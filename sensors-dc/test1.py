from picamera import PiCamera
from time import sleep
camera=PiCamera()
camera.start_preview()
for i in range (100);
camera.annotate_text = "Brightness : %d" %i
camera.brightness = i
sleep (0.1)
camera.stop_preview()
# Dung vong lap de thay doi do sang va chu thich tren man hinh muc sang hien tai