#!/usr/bin/env python

import pika
import sys
import cv2

if len(sys.argv) < 4:
	print "Not enough arguments!"
	sys.exit()

#getting file locations from sys.argv
dir1 = sys.argv[1]
img1 = cv2.imread(dir1)

dir2 = sys.argv[2]
img2 = cv2.imread(dir2)

result_dir = sys.argv[3]

if img2 is None or img1 is None:
	print "Image 1: " + ("Found" if img1 is None else "Not Found")
	print "Image 2: " + ("Found" if img2 is None else "Not Found")
	sys.exit()

try:
	connection = pika.BlockingConnection(pika.ConnectionParameters(
	        host='localhost'))

except pika.exceptions.ConnectionClosed:
	print "RabbitMQ Server not running"
	sys.exit()

channel = connection.channel()

channel.queue_declare(queue='img')
# channel.queue_declare(queue='dir')

channel.basic_publish(exchange='',
                      routing_key='img',
                      body=str(img1),
                      properties = pika.BasicProperties(content_type='image'))

channel.basic_publish(exchange='',
                      routing_key='img',
                      body=str(img2),
                      properties = pika.BasicProperties(content_type='image'))

# channel.basic_publish(exchange='',
#                       routing_key='dir',
#                       body=result_dir,
#                       properties = pika.BasicProperties(content_type='image'))

print("Sent messages successfully'")
connection.close()