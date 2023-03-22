import cv2 as cv
import numpy as np
import time

def my_eq(img):

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    hist, bins = np.histogram(gray.flatten(), 256, [0, 256])

    cdf = hist.cumsum()

    cdf_normalized = cdf * hist.max() / cdf.max()

    img2 = np.interp(gray.flatten(), bins[:-1], cdf_normalized)
    img2 = img2.reshape(img.shape[:2])
    img2 = np.uint8(img2)
    return img2


img = cv.imread('image.jpg')
print(type(img[0,0,0]))
start = time.time()
my_eq(img)
print('MyEqualizeHist time:', time.time() - start)

start2 = time.time()
cv.equalizeHist(img[:,:,0])
print('Opencv time :',time.time()-start2)