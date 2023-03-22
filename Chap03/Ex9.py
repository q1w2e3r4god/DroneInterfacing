import cv2 as cv

img = cv.imread('image.jpg')
patch = None
x1, y1, x2, y2 = -1, -1, -1, -1

def mouse_callback(event, x, y, flags, param):
    global patch, x1, y1, x2, y2
    if event == cv.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
    elif event == cv.EVENT_LBUTTONUP:
        x2, y2 = x, y
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        patch = img[y1:y2, x1:x2, :]
        patch1 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_NEAREST)
        patch2 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)
        patch3 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_CUBIC)
        cv.imshow('Resize nearest', patch1)
        cv.imshow('Resize bilinear', patch2)
        cv.imshow('Resize bicubic', patch3)

cv.namedWindow('Original')
cv.setMouseCallback('Original', mouse_callback)

while True:
    cv.imshow('Original', img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv.destroyAllWindows()