#!/usr/bin/env python
import pika
import numpy as np
import cv2

def dir_callback(ch, method, properties, body):
	global output_dir
	output_dir = body
	print(output_dir)

def callback(ch, method, properties, body):
	global img1, img2, lock
	nparr = np.fromstring(body, np.uint8)
	img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	while lock == True:
		time.sleep(1)
	lock = True

	if img1 is None:
		img1 = img_np
	elif img2 is None:
		img2 = img_np
	print "img 1 %r img 2 %r" % (img1 is None, img2 is None)
	if not(img1 is None or img2 is None):
		register(img1, img2)
	lock = False

def register(img1, img2):
	 
	# Convert images to grayscale
	img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
	img2_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	 
	# Find size of image1
	sz = img1.shape
	warp_mode = cv2.MOTION_TRANSLATION

	warp_matrix = np.eye(2, 3, dtype=np.float32)
	 
	# Specify the number of iterations.
	number_of_iterations = 5000;
	 
	# Specify the threshold of the increment
	# in the correlation coefficient between two iterations
	termination_eps = 1e-10;
	 
	# Define termination criteria
	criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, number_of_iterations,  termination_eps)
	 
	# Run the ECC algorithm. The results are stored in warp_matrix.
	(cc, warp_matrix) = cv2.findTransformECC(img1_gray,img2_gray,warp_matrix, warp_mode, criteria)
	
	img2_aligned = cv2.warpAffine(img2, warp_matrix, (sz[1],sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP);

	while output_dir is None:
		time.sleep(1)
	cv2.imwrite(output_dir, img2_aligned)
	# Show final results
	cv2.imshow("Image 1", img1)
	cv2.imshow("Image 2", img2)
	cv2.imshow("Aligned Image 2", img2_aligned)
	cv2.waitKey(0)
	# save results


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='img')
channel.queue_declare(queue='dir')
global img1, img2, lock, output_dir
img1 = None
img2 = None
lock = False
output_dir = None


channel.basic_consume(callback,
                      queue='img',
                      no_ack=True)
channel.basic_consume(dir_callback,
                      queue='dir',
                      no_ack=True)

channel.start_consuming()





#nparr = np.fromstring(img_str, np.uint8)
#img_np = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1
#http://stackoverflow.com/questions/17170752/python-opencv-load-image-from-byte-string