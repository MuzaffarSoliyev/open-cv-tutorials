import cv2

# vid_capture = cv2.VideoCapture('videos/sample-mp4-file-small.mp4')
vid_capture = cv2.VideoCapture('image_sequence/image_%04d.jpg')

if not vid_capture.isOpened():
    print('Error opening the video file')
else:
    fps = vid_capture.get(cv2.CAP_PROP_FPS)
    print('Frames per second : ', fps, 'FPS')

    frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print('Frame count : ', frame_count)

while vid_capture.isOpened():

    ret, frame = vid_capture.read()
    if ret:
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(20)

        if key == ord('q'):
            break
    else:
        break

vid_capture.release()
cv2.destroyAllWindows()
