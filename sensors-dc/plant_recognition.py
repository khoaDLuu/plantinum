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

MODEL_PATH = "planttype.model"
print("[INFO] loading model...")
model = load_model(MODEL_PATH)
camera = PiCamera()
rawCapture = PiRGBArray(camera)
time.sleep(0.1)
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
image = cv2.resize(image, (64, 64))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

prediction = model.predict(image)[0]

labels = ('succulent', 'palmplant', 'flower', 'foliageplant')
pred_dict = list(zip(labels, tuple(prediction)))
(label, proba) = max(pred_dict, key=lambda item: item[1])

print(label)
print(proba)



