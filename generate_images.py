import cv2

vid_capture = cv2.VideoCapture(0)

number = 0

while True:
    ret, frame = vid_capture.read(cv2.IMREAD_UNCHANGED)
    if ret:
        name = ''
        name += str(number)
        name = '0' * (4 - len(name)) + name
        cv2.imshow('Frame', frame)
        # cv2.imwrite('image_sequence/image_' + name + '.jpg', frame)
        number += 1

    if number == 1000:
        break

    if cv2.waitKey(20) == ord('q'):
        break
