import sys
import cv2
import numpy as np
import cv

if len(sys.argv) < 4:
	print "Not enough arguments!"
	sys.exit()

img1 = None
img2 = None
#getting file locations from sys.argv
dir1 = sys.argv[1]
with open(dir1, "rb") as imageFile:
  f = imageFile.read()
  img1 = bytearray(f)

dir2 = sys.argv[2]
with open(dir1, "rb") as imageFile:
  f = imageFile.read()
  img2 = bytearray(f)

print cv.phaseCorrelate(img1, img2)