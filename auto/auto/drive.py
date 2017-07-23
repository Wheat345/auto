#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)


myMotorEngine = mh.getMotor(1)
myMotorWheel = mh.getMotor(4)

#forward and then backword
myMotorEngine.setSpeed(50)
myMotorEngine.run(Adafruit_MotorHAT.FORWARD);

time.sleep(3)
myMotorEngine.run(Adafruit_MotorHAT.BACKWARD);


#break for 5 seconds
time.sleep(3)

# turn left
myMotorWheel.setSpeed(150)
myMotorWheel.run(Adafruit_MotorHAT.FORWARD);
myMotorEngine.run(Adafruit_MotorHAT.FORWARD);

time.sleep(1.5)

# turn right
myMotorWheel.run(Adafruit_MotorHAT.BACKWARD);

# turn on motor

time.sleep(1.5)
myMotorEngine.run(Adafruit_MotorHAT.RELEASE);
myMotorWheel.run(Adafruit_MotorHAT.RELEASE);












