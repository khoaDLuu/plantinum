# Setup for Rasberry Pi

## Hardware

### Preparation

* Raspberry Pi 3 B+
* Power Adapter for RPi
* RPi Camera Module
* Case, fan and heatsinks

### Installation
* Prepare for RPi OS install: https://www.raspberrypi.org/software/
* Follow this tutorial: https://www.raspberrypi.org/documentation/computers/getting-started.html

## System configuration

* Enable SSH

## Python library installation

* Install OpenCV
  * Note: This project doesn't need to use Python virtual environment, so skip any step related to venv
  * Note: The recommended swap size for setup is 1024MB
  * Follow the instructions in [this article to install OpenCV on RPi](https://qengineering.eu/install-opencv-4.2-on-raspberry-pi-4.html)

* Install tensorflow
  * `sudo apt-get update`
  * `pip3 install tensorflow`

* Install HDF5 + h5py
  * `sudo apt-get install libhdf5-serial-dev`
  * `pip3 install h5py`

* Install ML-related packages
  * `pip3 install pillow imutils`
  * `pip3 install scipy --no-cache-dir`
  * `pip3 install keras==2.3.1`

## LeNet archtecture
![LeNet](https://user-images.githubusercontent.com/46435936/131597300-65aefda9-ccac-4186-a3ad-a8de01bc8695.png)

## References
* [Tutorial of Image Recognition and RPi](https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/)
* [How to install OpenCV on RPi](https://qengineering.eu/install-opencv-4.2-on-raspberry-pi-4.html)
