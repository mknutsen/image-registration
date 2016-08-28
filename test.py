import sys
import cv2
import numpy as np
import cv

if len(sys.argv) < 4:
	print "Not enough arguments!"
	sys.exit()

#getting file locations from sys.argv
dir1 = sys.argv[1]
# # img1 = cv2.imread(dir1)

# dir2 = sys.argv[2]
# img2 = cv2.imread(dir2)

# result_dir = sys.argv[3]

# if img2 is None or img1 is None:
# 	print "Image 1: " + ("Found" if img1 is None else "Not Found")
# 	print "Image 2: " + ("Found" if img2 is None else "Not Found")
# 	sys.exit()

with open(dir1, "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)

file_bytes = np.asarray(b, dtype=np.uint8)
print len(file_bytes)
img_data_ndarray = cv2.imdecode(file_bytes,0)


# img_str = bytearray(img1)
# file_bytes = np.asarray(img_str, dtype=np.uint8)
# print len(file_bytes)
# img_data_ndarray = cv2.imdecode(file_bytes,0)


# ncols = len(img1)
# nrows = len(img1[0])

# img_str = np.fromstring ( str(img1), np.uint8 )

# nparr = np.fromstring(str(img1), dtype=np.uint8)#.reshape(nrows, ncols, 3)
# img_np = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)

print img_data_ndarray