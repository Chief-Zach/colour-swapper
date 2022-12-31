import cv2
import numpy as np

image = cv2.imread("img.png")
image[np.where((image!=[0,0,0]).all(axis=2))] = [255,0,150]
cv2.imwrite('red.png', image)