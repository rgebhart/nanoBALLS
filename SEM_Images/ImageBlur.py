import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('TestBlur.TIF')
kernel = (11,11)

#Averaging
avg_blur = cv.blur(img,kernel)
#Gaussian Blurring
gauss_blur = cv.GaussianBlur(img,kernel,0)
#Median Blurring
median_blur =cv.medianBlur(img,5)
#Bilateral Filtering
Bi_blur = cv.bilateralFilter(img,9,75,75)

fig, ((ax1,ax2,ax3),(ax4,ax5,ax6)) = plt.subplots(2,3,figsize = (50,50))

ax1.imshow(img)
ax1.title.set_text('Original')

ax2.imshow(avg_blur)
ax2.title.set_text('avg_blur')

ax3.imshow(gauss_blur)
ax3.title.set_text('gauss_blur')

ax4.imshow(median_blur)
ax4.title.set_text('median_blur')

ax5.imshow(Bi_blur)
ax5.title.set_text('Bi_blur')

plt.show()