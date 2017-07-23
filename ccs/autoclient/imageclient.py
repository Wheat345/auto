from PIL import Image
from time import gmtime, strftime
import websocket
import cStringIO
import base64
import thread
import time
import tensorflow as tf
import sys


class WSClient():#TF

    def __init__(self):
        #self.count = 1
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp("ws://192.168.0.101:8888/ws",
        on_message = self.on_message,
        on_error = self.on_error,
        on_close = self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def on_message(self, ws, message):
        #print "message from server"
        image_string = cStringIO.StringIO(base64.b64decode(message))
        image = Image.open(image_string)
        #image.show()
        image.save("savedimage.png") # image saved
        #time.sleep(0.25)
        #image.save("savedimage"+self.count+".png") # image saved
        #self.count = self.count +1
        #print message;
        print "image saved"

    def on_error(self, ws, error):
        print error

    def on_close(self, ws):
        print "connection closed"

    def on_open(self, ws):
        print "connected"
        def run(*args):
            #for i in range(10):
            while (True):
                ws.send("client needs pic ")
            time.sleep(3)
            ws.send("stop")
            ws.close()
            print("thread terminating...")
        thread.start_new_thread(run, ())


if __name__ == "__main__":
    client = WSClient()
