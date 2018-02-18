import cv2
import numpy as np

image = cv2.imread('Lenna.png')

#making a square
square = np.zeros((300,300), np.uint8)
cv2.rectangle(square, (50,50),(250,250),255, -2)
cv2.imshow('Square', square)

#making ellipse
ellipse = np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse, (150,150), (150,150), 30, 0, 180, 255, -1)
cv2.imshow('Ellipse', ellipse)


#show only where they intersectd 
And = cv2.bitwise_and(square, ellipse)
cv2.imshow('And',And)

bitwiseOr = cv2.bitwise_or(square, ellipse)
cv2.imshow('Or',bitwiseOr)

bitwiseXor = cv2.bitwise_xor(square, ellipse)
cv2.imshow('Xor',bitwiseXor)

bitwiseNot_sq = cv2.bitwise_not(square)
cv2.imshow('NOT - square',bitwiseNot_sq)

cv2.waitKey(0)
cv2.destroyAllWindows()
