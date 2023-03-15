import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit('카메라를 찾을 수 없습니다.')

frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
    cv.imshow('Video Display', frame)
    key = cv.waitKey(1)
    if key == ord('c'):
        frames.append(frame)
    elif key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()    

frame_concat = 3
if len(frames) > 0:
    count = 0
    while len(frames) > 0:
        if count == 0:
            imgs = frames[0]
            frames.pop(0)
        else:
            imgs = np.hstack((imgs, frames[0]))
            frames.pop(0)
        count += 1
        if count == frame_concat or len(frames) == 0:
            cv.imshow('Collected Images', imgs)
            cv.waitKey()
            cv.destroyAllWindows()
            count = 0
    frames.clear()