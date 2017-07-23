from PIL import Image
from time import gmtime, strftime
import websocket
import cStringIO
import base64
import thread
import time
import tensorflow as tf
import sys
import os


class WSClient():#TF

    def __init__(self):
        #with open("imagefromclient.png", "rb") as imageFile:
        #    self.str = base64.b64encode(imageFile.read())
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp("ws://192.168.0.101:8889/ws",
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
        #print message;
        #print "image saved"

    def on_error(self, ws, error):
        print error

    def on_close(self, ws):
        print "connection closed"

    def on_open(self, ws):
        print "connected"
        def run(*args):
            for i in range(10):

                #ws.send("hello from client")
                ws.send(classify.classifyimage())
                #time.sleep(1)

            #ws.send(classify.classifyimage())
            #print (strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            time.sleep(3)
            ws.send("stop")
            ws.close()
            print("thread terminating...")
        thread.start_new_thread(run, ())

class Classify():
    def __init__(self):
        self.command = ""
        self.scoremap = {"nothing" : 0  }

    def classifyimage(self):
        # change this as you see fit
        image_path = sys.argv[1]

        # Read in the image_data
        image_data = ""
        if os.path.exists(image_path) and os.path.getsize(image_path) > 0:
            image_data = tf.gfile.FastGFile(image_path, 'rb').read()
        else:
            return "stop"
        #if (image_data == None):
        #    return "stop"
        # Loads label file, strips off carriage return
        label_lines = [line.rstrip() for line
                           in tf.gfile.GFile("retrained_labels.txt")]

        # Unpersists graph from file
        with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            predictions = sess.run(softmax_tensor, \
                         {'DecodeJpeg/contents:0': image_data})
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                self.scoremap.update({human_string: score})
                #print (node_id)
                #print('%s (score = %.5f)' % (human_string, score))
        self.scoremap = sorted(self.scoremap.items(), key=lambda x: x[1])
        self.command = ''.join(map(str, self.scoremap) [-1])
        self.scoremap = {"nothing" : 0  }
        #time.sleep(3)
        print self.command
        return self.command

if __name__ == "__main__":
    classify = Classify()
    client = WSClient()
    #classify.classifyimage()
