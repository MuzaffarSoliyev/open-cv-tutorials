import cv2
import numpy as np

img = cv2.imread('images/input-image-for-demo-throughout-1024x682.jpg')
print(img.shape)
cv2.imshow('Original Image', img)

cropped_image = img[80:280, 150:330]

cv2.imshow('Cropped image', cropped_image)

cv2.imwrite('images/cropped-image.jpg', cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
