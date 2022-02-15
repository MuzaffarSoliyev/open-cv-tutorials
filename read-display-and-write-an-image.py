import cv2


img_grayscale = cv2.imread('images/input-image-for-demo-throughout-1024x682.jpg', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('images/input-image-for-demo-throughout-1024x682.jpg', cv2.IMREAD_COLOR)
img_unchanged = cv2.imread('images/input-image-for-demo-throughout-1024x682.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('grayscale image', img_grayscale)
cv2.imshow('color image', img_color)
cv2.imshow('unchanged image', img_unchanged)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('images/grayscale.jpg', img_grayscale)
