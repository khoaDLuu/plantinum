from picamera import PiCamera
from time import sleep

camera = PiCamera()
for i in range(̀5):  # take 5 consecutive photos
    sleep(3)
    camera.capture(f'test-imgs/test{i}.jpg')
