#!/usr/bin/env python
import sys
import cv2
import numpy as np
import consumer

img1 = None
img2 = None
#getting file locations from sys.argv
dir1 = "1.png"
with open(dir1, "rb") as imageFile:
  f = imageFile.read()
  img1 = bytearray(f)

dir2 = "2.png"
with open(dir2, "rb") as imageFile:
  f = imageFile.read()
  img2 = bytearray(f)

nparr_1 = np.fromstring(str(img1), np.uint8)
np_img_1 = cv2.imdecode(nparr_1, cv2.IMREAD_COLOR)

nparr_2 = np.fromstring(str(img2), np.uint8)
np_img_2 = cv2.imdecode(nparr_2, cv2.IMREAD_COLOR)

consumer.register(np_img_1, np_img_2, "aligned.png")