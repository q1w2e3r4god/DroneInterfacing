import cv2 as cv
import sys

file_name = 'media/smile_girl.jpg' # for jupyter or ipython(spyder)
img = cv.imread(file_name)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))

def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x,y), (x+200, y+200), (0, 0, 255), 2)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), 50, (255, 0, 0), 2)
    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while(True):
    if cv.waitKey(1) == ord('q'):        
        cv.destroyAllWindows()
        break
