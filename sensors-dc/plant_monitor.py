from serial import Serial
import RPi.GPIO as GPIO
import requests
from dotenv import load_dotenv

from plant_recognition import guess_planttp
from cldn_uploading import upload_to_cldn
from picam import take_photo
from sensor_read import read_sensor
from sdata_sending import send_to_server
from led_control import LedControl


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

load_dotenv()


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
        pass

    def add_plant(self):
        try:
            r = requests.post(
                f'{self.base_url}/plants',
                json=data,
                auth=self._auth
            )
            self.plant_id = r.json()['username']
            print(r.json())
        except:
            raise

    def submit_sensor_data(self, data):
        try:
            r = requests.post(
                f'{self.base_url}/plants/{self.plant_id}/sensor_data',
                json=data,
                auth=self._auth
            )
            print(r)
        except:
            raise


class SerialCom:
    def __init__(self, port="/dev/ttyACM0", rate=9600):
        self.ser_to_ardn = Serial(port, rate)

    def send_start_sig(self):
        self.ser_to_ardn.write(b'u')

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
    def __init__(self, serial_com, ind_led):
        self.ardn_com = serialcom
        self.indicator_led = ind_led
        self.plant_existed = False

    def start(self):
        self.ardn_com.send_start_sig()

    def run(self):
        self.start()
        
        while True:
            try:
                if self.ardn_com.pot_sig():
                    pass
                else:
                    pass

            except BadSerialSignal:
                pass
            
            except KeyboardInterrupt:
                GPIO.cleanup()
                raise

            except Exception:
                raise


if __name__ == '__main__':
    indicator_led = LedControl()
    serial_communicator = SerialCom()
    api = APICom('https://plantinum-stage.herokuapp.com', plant_id=10)
    monitor = PlantMonitor(serial_communicator, indicator_led)

    monitor.run()

    GPIO.cleanup()
