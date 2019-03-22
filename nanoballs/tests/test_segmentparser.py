# Imports
import cv2
import numpy as np
import pandas as pd
from skimage.measure import regionprops
import segmentparser
import random

# Creating test inputs for testing purposes.
img = cv2.imread('SEM_Images/Opal_Tecopa_near_gem.jpg')
img = np.array(img, dtype=np.uint8)
kernel = np.ones((5,6), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
canny = cv2.Canny(opening,100,150,3,L2gradient=True)
ret, thresh = cv2.threshold(canny,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
D_bf_cv = ndimage.distance_transform_bf(thresh)
localMax = peak_local_max(D_bf_cv, indices=False, min_distance=10,labels=thresh)
markers_cv = ndimage.label(localMax)[0]
labels_bf_cv = watershed(-D_bf_cv, markers_cv, mask=thresh)

def test_segmentparser():
    """Unit test for the segmentparser.py function"""
    output = segmentparser(labels_bf_cv, thresh)
    # Creating some random numbers to play with.
    rows, columns = output.shape
    location = random.randint(1,rows-1)

    # Testing whether or not the output is pandas dataframe or not
    assert isinstance(output, pd.DataFrame) == True
    
    # Testing to make sure that all returned values are real
    # ----------------------
    # Making sure the x coordinate is within the image
    assert int(output.loc[location,1]) > 0
    # Making sure the y coordinate is within the image
    assert int(output.loc[location,2]) > 0
    # Any area should be greater than zero
    assert int(output.loc[location,3]) > 0
