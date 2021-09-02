# PLANTINUM
Smart indoor plant monitoring system

## Features
* Plant type recognition for proper watering
  * Succulent
  * Palmplant
  * Flower
  * Foliage plant
* Environmental data gathering
  * Temperature
  * Humidity
  * Light intensity
  * Soil moisture
* Simple watering system
* Environment data and plant photo display on mobile app
* Simple plant leave problem detection (currently not working very well)
* Alerting LED

## Nice-to-have features
* Environment data stats and visualization
* Improved plant leave problem detection
* Auto lighting
* Multi-plant monitoring
* Plant time-lapse video generation

## Architecture and Design
### Data flow
![dataflow](https://user-images.githubusercontent.com/46435936/131373533-f7ab8b5e-1e64-4eb7-8bd1-f135314a87ae.png)

### Hardware component assembly
![circuit wiring](https://user-images.githubusercontent.com/46435936/131376822-c9dd440f-9a64-415f-9f07-f7c5245636c2.png)

## Installation

* Clone the project
```
git clone git@github.com:khoaDLuu/plantinum.git
```
* Set up React Native app for [mobile app](./mobile-ui/README.md)
* Set up Python for [API server](./server-api/README.md)
* Set up [Arduino and Rasberry Pi](./sensors-dc/README.md) environments

## References
* [Tutorial of Image Recognition and RPi](https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/)
* [How to install OpenCV on RPi](https://qengineering.eu/install-opencv-4.2-on-raspberry-pi-4.html)
