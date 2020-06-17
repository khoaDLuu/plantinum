import time

import requests
import serial
import json
from sensor_read import read_sensor
from cldn_uploading import upload_to_cldn
from picam import take_photo

# change ACM number as found from ls /dev/tty/ACM*
ser = serial.Serial("/dev/ttyACM0", 9600)
ser.baudrate = 9600
sensor_data = read_sensor()
image_url = upload_to_cldn(take_photo())
data = {
        "temperature": sensor_data[0],
        "humidity": sensor_data[1],
        "moisture": sensor_data[2],
        "light_intensity": sensor_data[3],
        "img_url": image_url
    }

try:
    r = requests.post(
        'https://plantinum-stage.herokuapp.com/plants/1/sensor_data',
        json=data
    )
    print(r)
except:
    raise

