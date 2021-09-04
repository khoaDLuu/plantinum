import time
import logging

from serial import Serial
import RPi.GPIO as GPIO
import requests
from dotenv import load_dotenv

from planttp_recognition import guess_planttp
from cldn_uploading import upload_to_cldn
from picam import take_photo
# from sensor_read import read_sensor
from sdata_sending import send_to_server
from led_control import LedControl


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log', filemode='w',
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s'
)


class BadSerialSignal(Exception):
    """Exception raised for errors reading serial signal.

    Attributes:
        signal -- serial signal causing the error
        message -- explanation of the error
    """

    def __init__(self, signal, message="Unrecognized signal"):
        self.signal = signal
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'signal={self.signal} --> {self.message}'


class APICom:
    def __init__(self, base_url, plant_id=1):
        self._auth = (os.getenv("MAIN_API_USERNAME"), os.getenv("MAIN_API_PASSWORD"))
        self.base_url = base_url
        self.plant_id = plant_id

    def get_auth_token(self):
        # TODO: Implement this to use token instead of password
        pass

    def add_plant(self, data):
        try:
            r = requests.post(
                f'{self.base_url}/plants',
                json=data,
                auth=self._auth
            )
            self.plant_id = r.json()['plant_id']
            logging.debug(r.json())
        except Exception as e:
            logging.error(
                "Exception occurred when adding new plant",
                exc_info=True
            )

    def submit_sensor_data(self, data):
        try:
            r = requests.post(
                f'{self.base_url}/plants/{self.plant_id}/sensor_data',
                json=data,
                auth=self._auth
            )
            logging.debug(r.json())
        except Exception as e:
            logging.error(
                "Exception occurred when submitting sensor data",
                exc_info=True
            )


class SerialCom:
    def __init__(self, port="/dev/ttyACM0", rate=9600):
        self.ser_to_ardn = Serial(port, rate)

    def send_start_sig(self):
        self.ser_to_ardn.write(b'u')

    def send_data_ready_sig(self):
        self.ser_to_ardn.write(b'1')

    def pot_sig(self):
        potd_sig = self.ser_to_ardn.readline()
        if potd_sig == b'Detected\r\n':
            return True
        elif potd_sig == b'Nothing\r\n':
            return False
        else:
            raise BadSerialSignal(
                potd_sig,
                message=("Unrecognized signal: "
                         "neither Detected nor Nothing")
            )

    def read_sensor(self):
        str_temp = self.ser_to_ardn.readline()
        temp = float(str_temp)
    
        str_humi = self.ser_to_ardn.readline()
        humi = float(str_humi)
        
        str_light = self.ser_to_ardn.readline()
        light = int(str_light)
        
        str_mois = self.ser_to_ardn.readline()
        mois = int(str_mois)

        return temp, humi, light, mois

    def data_ready_sig(self):
        data_ready_sig = self.ser_to_ardn.readline()
        if data_ready_sig == b'Ready\r\n':
            return True
        else:
            raise BadSerialSignal(
                data_ready_sig,
                message=("Unrecognized signal: not Ready")
            )


class PlantMonitor:
    def __init__(self, serial_com, api, ind_led):
        self.ardn_com = serial_com
        self.remote_api_com = api
        self.indicator_led = ind_led
        self.plant_existed = False

    def start(self):
        self.ardn_com.send_start_sig()

    def shake_hands(self):
        if self.ardn_com.pot_sig():
            plant_img = take_photo()
            label, _ = guess_planttp(plant_img)
            if label != 'unknown':
                self.plant_existed = True
                self.indicator_led.on()
                self.ardn_com.send_data_ready_sig()
                return True
            else:
                self.plant_existed = False
                return False
        else:
            self.plant_existed = False
            self.indicator_led.off()
            return False

    def communicate(self):
        while True:
            try:
                plant_img = take_photo()
                img_url = upload_to_cldn(plant_img, folder='planttype')
                sensor_data = self.read_sensor()

                self.remote_api_com.submit_sensor_data({
                    "temperature": sensor_data[0],
                    "humidity": sensor_data[1],
                    "moisture": sensor_data[2],
                    "light_intensity": sensor_data[3],
                    "img_url": image_url
                })
                time.sleep(1)
            
            except ValueError as e:
                logging.warn(
                    f"An error occurred: {e}\nRetrying...",
                    exc_info=True
                )

            # except ConnectingError:
            #     pass

    def run(self):
        self.start()

        while True:
            try:
                if self.shake_hands():
                    self.communicate()

            except BadSerialSignal as e:
                logging.warn(
                    f"An error occurred: {e}\nRetrying...",
                    exc_info=True
                )
            
            except KeyboardInterrupt:
                GPIO.cleanup()
                raise

            except Exception:
                logging.exception(f"An error occurred: {e}\nRetrying...")


if __name__ == '__main__':
    indicator_led = LedControl()
    serial_communicator = SerialCom()
    api = APICom('https://plantinum-stage.herokuapp.com', plant_id=10)
    monitor = PlantMonitor(serial_communicator, api, indicator_led)

    monitor.run()

    GPIO.cleanup()
