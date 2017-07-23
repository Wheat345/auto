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


class Camera():
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (320, 240)


class WebSocketHandler(tornado.websocket.WebSocketHandler):#image from car

    def open(self):
        print 'new connection'
    def on_message(self, message):
        print "message from client"
        print message
        sio = io.StringIO()
        camera.camera.capture(sio, "png", use_video_port=True)
        self.write_message(base64.b64encode(sio.getvalue()))
    def on_close(self):
        print 'connection closed'

if __name__ == '__main__':
    camera = Camera()
    application = tornado.web.Application([
    (r'/ws', WebSocketHandler),
    ])

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

