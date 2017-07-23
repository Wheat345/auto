#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit

class Move():
    def __init__(self):
        # create a default object, no changes to I2C address or frequency
        self.mh = Adafruit_MotorHAT(addr=0x60)
        #self.turnOfFMotors = turnOffOmotor()
        #atexit.register(self.turnOffMotors())
        self.myMotorEngine = self.mh.getMotor(1)
        self.myMotorWheel = self.mh.getMotor(4)
        self.myMotorEngine.run(Adafruit_MotorHAT.RELEASE)
        self.myMotorWheel.run(Adafruit_MotorHAT.RELEASE)

    def forward(self):
        #forward and then backword
        self.myMotorEngine.setSpeed(50)
        self.myMotorEngine.run(Adafruit_MotorHAT.FORWARD);

    def backwoard(self):
        #time.sleep(3)
        self.myMotorEngine.setSpeed(50)
        self.myMotorEngine.run(Adafruit_MotorHAT.BACKWARD);

    def turnleft(self):
        # turn left
        self.myMotorWheel.setSpeed(150)
        self.myMotorWheel.run(Adafruit_MotorHAT.FORWARD);
        self.myMotorEngine.run(Adafruit_MotorHAT.FORWARD);

    def turnleft(self):
        # turn left
        self.myMotorWheel.setSpeed(150)
        self.myMotorWheel.run(Adafruit_MotorHAT.BACKWARD);
        self.myMotorEngine.run(Adafruit_MotorHAT.BACKWARD);

    def release(self):
        self.myMotorEngine.run(Adafruit_MotorHAT.RELEASE);
        self.myMotorWheel.run(Adafruit_MotorHAT.RELEASE);

if __name__ == "__main__":
    move = Move()

