from keras.preprocessing.image import img_to_array
from keras.models import load_model
from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread
import numpy as np
import imutils
import time
import cv2
import os

from planttp_recognition import guess_planttp


MODEL_PATH = "planttype.model"

camera = PiCamera()
rawCapture = PiRGBArray(camera)
time.sleep(0.1)
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

label, proba = guess_planttp(image, MODEL_PATH)

print(label)
print(proba)



