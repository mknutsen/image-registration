#!/usr/bin/env python
import pika
import numpy as np
import cv2
def register(img1, img2):
	print ("got em both")
	print img1
	print img2
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='img')
channel.queue_declare(queue='dir')
global img1, img2, lock
img1 = None
img2 = None
lock = False

def callback(ch, method, properties, body):
	global img1, img2, lock
	nparr = np.fromstring(body, np.uint8)
	img_np = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
	print nparr
	while lock == True:
		time.sleep(1)

	lock = True

	if img1 is None:
		img1 = img_np
	elif img2 is None:
		img2 = img_np
	print "img 1 %r img 2 %r" % (img1, img2)
	if not(img1 is None or img2 is None):
		register(img1, img2)

	lock = False

channel.basic_consume(callback,
                      queue='img',
                      no_ack=True)

channel.start_consuming()





#nparr = np.fromstring(img_str, np.uint8)
#img_np = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1
#http://stackoverflow.com/questions/17170752/python-opencv-load-image-from-byte-string