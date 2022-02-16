import cv2
import numpy as np

image = cv2.imread('images/image-e1619470839641-1024x353.jpg')

h, w, x = image.shape
# print(h, w, x)

down_width = 300
down_height = 200

down_points = (down_width, down_height)
resize_down = cv2.resize(image, down_points, interpolation=cv2.INTER_AREA)
cv2.imshow('Resized', resize_down)
cv2.waitKey(0)
coefficient_x = 2.0
coefficient_y = 2.0
resize_up = cv2.resize(image, None, fx=coefficient_x, fy=coefficient_y, interpolation=cv2.INTER_NEAREST)

cv2.imshow('Resized', resize_up)

cv2.waitKey(0)
cv2.destroyAllWindows()