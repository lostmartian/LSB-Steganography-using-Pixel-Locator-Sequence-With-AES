import cv2
from matplotlib import pyplot as plt
img1 = cv2.imread('images/out5.png', 1)
plt.hist(img1.ravel(),256,[0,256])
plt.show()
