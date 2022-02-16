import cv2

image = cv2.imread('images/input-image-for-demo-throughout-1024x682.jpg')
height, width, _ = image.shape
print(height, width)

for w in range(0, width, 32):
    for h in range(0, height, 31):
        tmp_image = image[h: h + 31, w: w + 32]
        cv2.imwrite(f'images/cropped_images/image_{w}-{h}.jpg', tmp_image)
