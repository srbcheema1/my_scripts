# Motion detector

From [this repository](https://github.com/pBouillon/Raspberry_ressources)

## What do you need ?

### Electronic

In order to build everything, you will need:
* 1x Breadboard
* 1x [HC-SR04 sensor](https://www.amazon.fr/ultrasons-HC-SR04-Capteur-distance-Arduino/dp/B00BIZQWYE/ref=sr_1_3?ie=UTF8&qid=1506950469&sr=8-3&keywords=HC-SR04)
* A bunch of cables
* A LED
* A [Raspberry Pi](https://www.raspberrypi.org/products/) 
* Some Resistances

### BCM Pins (see [differences with GPIO Pins](https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering)):
Connect the LED to the ground and the pin n°25 
Connect the HR-SR04 sensor with the pin n°7 as intput and n°8 as input

### Code usage
Run `motion_detector.py` and see on your screen the program calibrate himself
Everytime you will pass in front of your sensor, the LED turn on, then off and display a message

Feel free to custom your alert, for example by [sending an alert by mail](https://github.com/pBouillon/easy_mail).

## Disclaimer
This project was in order to discover electronic through the Raspberry and manipulate PINS.
It also aimed to use a third-party component (HC-SR04)
