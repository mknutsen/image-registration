import sys
import cv2
import numpy as np

img1 = None
img2 = None
#getting file locations from sys.argv
dir1 = "/Users/mknutsen/Desktop/1.png"
with open(dir1, "rb") as imageFile:
  f = imageFile.read()
  img1 = bytearray(f)

dir2 = "/Users/mknutsen/Desktop/2.png"
with open(dir2, "rb") as imageFile:
  f = imageFile.read()
  img2 = bytearray(f)

nparr_1 = np.fromstring(str(img1), np.uint8)
np_img_1 = cv2.imdecode(nparr_1, cv2.IMREAD_COLOR)

nparr_2 = np.fromstring(str(img2), np.uint8)
np_img_2 = cv2.imdecode(nparr_2, cv2.IMREAD_COLOR)
 
# Convert images to grayscale
np_img_1_gray = cv2.cvtColor(np_img_1,cv2.COLOR_BGR2GRAY)
np_img_2_gray = cv2.cvtColor(np_img_2,cv2.COLOR_BGR2GRAY)
 
# Find size of image1
sz = np_img_1.shape
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
(cc, warp_matrix) = cv2.findTransformECC(np_img_1_gray,np_img_2_gray,warp_matrix, warp_mode, criteria)
 
if warp_mode == cv2.MOTION_HOMOGRAPHY :
    # Use warpPerspective for Homography 
    np_img_2_aligned = cv2.warpPerspective (np_img_2, warp_matrix, (sz[1],sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
else :
    # Use warpAffine for Translation, Euclidean and Affine
    np_img_2_aligned = cv2.warpAffine(np_img_2, warp_matrix, (sz[1],sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP);
 
# Show final results
cv2.imshow("Image 1", np_img_1)
cv2.imshow("Image 2", np_img_2)
cv2.imshow("Aligned Image 2", np_img_2_aligned)
cv2.waitKey(0)