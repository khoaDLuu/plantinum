# network testing


# To test the network from terminal, make sure you are at rpi-dp/planttp-clfier/, if not cd there and run:
# python network_testing.py --model planttype.model --image test/test.jpg

import argparse

from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import imutils
import cv2

IMG_SIZE = 64

ap = argparse.ArgumentParser()
ap.add_argument(
    '-m', '--model', required=True,
    help='path to trained model'
)
ap.add_argument(
    '-i', '--image', required=True,
    help='path to input image'
)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
original = image.copy()

image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

print("[INFO] loading network...")
model = load_model(args["model"])

prediction = model.predict(image)[0]

labels = ('succulent', 'palmplant', 'flower', 'foliageplant','unknown')
pred_dict = list(zip(labels, tuple(prediction)))

(label, proba) = max(pred_dict, key=lambda item: item[1])
label_on_img = f"{label}: {proba * 100:.2f}%"

output = imutils.resize(original, width=400)
cv2.putText(
    output, label_on_img, (10, 25),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6, (255, 25, 0), 2
)

print(list(pred_dict))
cv2.imshow('Output image', output)
cv2.waitKey(0)

