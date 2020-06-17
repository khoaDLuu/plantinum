import argparse

from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import imutils
import cv2

import time
import picamera

def planttp_rec(image, model_path):
    IMG_SIZE = 64
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    model = load_model(model_path)

    prediction = model.predict(image)[0]

    labels = ('succulent', 'palmplant', 'flower', 'foliageplant')
    pred_dict = list(zip(labels, tuple(prediction)))

    (label, proba) = max(pred_dict, key=lambda item: item[1])
    return (label, proba)
