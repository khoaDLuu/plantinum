from picamera.array import PiRGBArray
from picamera import PiCamera

from planttp_recognition import guess_planttp


MODEL_PATH = "planttype.model"

camera = PiCamera()
rawCapture = PiRGBArray(camera)
time.sleep(0.1)
camera.capture(rawCapture, format="bgr")
image = rawCapture.array  # 3-dimensional numpy array

label, proba = guess_planttp(image, MODEL_PATH)

print(label)
print(proba)



