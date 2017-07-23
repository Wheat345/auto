from PIL import Image
from picamera import PiCamera
from time import sleep
from time import gmtime, strftime
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import cStringIO as io
import base64
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit


#class Camera():
#    def __init__(self):
#        self.camera = PiCamera()
#        self.camera.resolution = (320, 240)
    

class WebSocketHandler(tornado.websocket.WebSocketHandler):#car


        
    def open(self):
        print 'new connection'

    def on_message(self, message):
        print "message from client"
        print message
        #sio = io.StringIO()
        #camera.camera.capture(sio, "png", use_video_port=True)
        #self.write_message(base64.b64encode(sio.getvalue()))
        move.forward()
        if (message == "stop"):
            move.release()
        if "1forward" in message:
            print "move forward 1forward"
            move.release()
            move.forward()
            
        if "2leftturn" in message:
            print "left turn 2leftturn"
            #move.release()
            #time.sleep(0.5)
            move.turnleft()
            
        if "3leftturn" in message:
            print "left turn 3leftturn"
            #move.release()
            #time.sleep(0.5)
            move.turnleft()
            
        if "4leftturn" in message:
            print "left turn 4leftturn"
            #move.release()
            #time.sleep(0.5)
            move.turnleft()
            
        if "5forward" in message:
            print "move forwardkward5 forward"
            move.release()
            move.forward()
        
        
    def on_close(self):
        print 'connection closed'


#!/usr/bin/python

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
        self.myMotorEngine.setSpeed(65)
        self.myMotorEngine.run(Adafruit_MotorHAT.FORWARD);

    def backward(self):
        #time.sleep(3)
        self.myMotorEngine.setSpeed(75)
        self.myMotorEngine.run(Adafruit_MotorHAT.BACKWARD);

    def turnleft(self):
        # turn left
        self.myMotorEngine.setSpeed(70)
        self.myMotorWheel.setSpeed(150)
        self.myMotorWheel.run(Adafruit_MotorHAT.FORWARD);
        self.myMotorEngine.run(Adafruit_MotorHAT.FORWARD);

    def turnright(self):
        # turn right
        self.myMotorEngine.setSpeed(50)
        self.myMotorWheel.setSpeed(150)
        self.myMotorWheel.run(Adafruit_MotorHAT.BACKWARD);
        self.myMotorEngine.run(Adafruit_MotorHAT.BACKWARD);


    def release(self):
        self.myMotorEngine.run(Adafruit_MotorHAT.RELEASE);
        self.myMotorWheel.run(Adafruit_MotorHAT.RELEASE);

#if __name__ == "__main__":
#    move = Move()


if __name__ == '__main__':
    move = Move()
    #camera = Camera()
    application = tornado.web.Application([
    (r'/ws', WebSocketHandler),
    ])

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8889)
    tornado.ioloop.IOLoop.instance().start()

