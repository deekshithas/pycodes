
import cv2
import numpy as np
img=cv2.imread("flower.jpg")
cv2.imshow("original",img)
cv2.waitKey(0)
M=np.ones(img.shape,dtype="uint8")*150
added=cv2.add(img,M)
cv2.imshow("added",added)

subtracted=cv2.subtract(img,M)
cv2.imshow("subtract",subtracted)

mul=cv2.multiply(img,M)
cv2.imshow("multiply",mul)

cv2.waitKey(0)
cv2.destroyAllWindows()




