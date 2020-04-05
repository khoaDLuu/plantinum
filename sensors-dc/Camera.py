from picamera import PiCamera
from time import sleep
camera=PiCamera()
camera.start_preview()
for i in range(5):                                         #chụp 5 ảnh liên tiếp
    sleep(5)
    camera.capture('/home/pi/Desktop/image%d.jpg'%i)
camera.stop_preview()

