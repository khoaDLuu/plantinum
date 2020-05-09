import time

from picamera.array import PiRGBArray
from picamera import PiCamera

def take_photo():
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)
    time.sleep(0.1)
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    return image

