# network training
# based on this article on pyimagesearch
# https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/

# To train the network from terminal, make sure you are at rpi-dp/planttp-clfier/, if not cd there and run:
# python network_training.py --dataset dataset --model planttype.model

import os
import argparse
import random

import numpy as np
import cv2
from imutils import paths
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
from lenet import LeNet
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


# Parsing terminal command
ap = argparse.ArgumentParser()
ap.add_argument(
    '-d', '--dataset', required=True,
    help='path to input dataset'
)
ap.add_argument(
    '-m', '--model', required=True,
    help='path to output model'
)
ap.add_argument(
    '-p', '--plot', type=str, default='test/plot.png',
    help='path to output accuracy/lost plot'
)
args = vars(ap.parse_args())

# Set variables, initializing ...
EPOCHS = 25
INIT_LR = 1e-3
BS = 32

print('[INFO] loading images...')
data = []
labels = []
label_codes = {
    'succulent': 0,
    'palmplant': 1,
    'flower': 2,
    'foliageplant': 3
}

# find all image paths (in all dir levels)
image_paths = sorted(list(
    paths.list_images(args['dataset'])
))

random.seed(48)
random.shuffle(image_paths)

for image_path in image_paths:
    image = cv2.imread(image_path)
    image = cv2.resize(image, (28, 28))
    image = img_to_array(image)
    data.append(image)

    label = image_path.split(os.path.sep)[-2]
    label = label_codes[label]
    labels.append(label)

data = np.array(data, dtype='float') / 255.0
labels = np.array(labels)

(trainD, testD, trainL, testL) = train_test_split(
    data,
    labels,
    test_size=0.25,
    random_state=35
)

trainL = to_categorical(trainL, num_classes=4)
testL = to_categorical(testL, num_classes=4)

aug = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

print('[INFO] compiling model...')
model = LeNet.build(
    width=28, height=28, depth=3, classes=4
)
opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(
    loss='categorical_crossentropy',
    optimizer=opt,
    metrics=['accuracy']
)

print('[INFO] training network...')
H = model.fit_generator(
    aug.flow(trainD, trainL, batch_size=BS),
    validation_data=(testD, testL),
    steps_per_epoch=len(trainD) // BS,
    epochs=EPOCHS,
    verbose=1
)

print('[INFO] serializing network...')
model.save(args['model'])

plt.style.use('ggplot')
plt.figure()
N = EPOCHS
plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, N), H.history["accuracy"], label="train_acc")
plt.plot(np.arange(0, N), H.history["val_accuracy"], label="val_acc")
plt.title("Training Loss and Accuracy on Plant Type problem")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="lower left")
plt.savefig(args["plot"])
