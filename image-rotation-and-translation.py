import cv2
import numpy as np

image = cv2.imread('images/image-15.png')

height, width, _ = image.shape
print(height, width)
# exit()

center = (width / 2, height / 2)

rotate_matrix = cv2.getRotationMatrix2D(center, angle=45, scale=1.5)

rotate_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))

cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotate_image)

# translation image

tx, ty = width / 4, height / 4

translate_matrix = np.array([
    [1, 0, -tx],
    [0, 1, ty]
], dtype=np.float32)

translated_image = cv2.warpAffine(image, M=translate_matrix, dsize=(width, height))

cv2.imshow('Translated image', translated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
