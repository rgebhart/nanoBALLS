import cv2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import argparse
from skimage.measure import label
from skimage.measure import regionprops

def segmentparser(segmented_image, binary):
    """Takes an edge detected image and an image binary and returns a Pandas dataframe of the x-y coordinates and area of the image segments.  Both the edge detected image and the binary of the image should be 1D image files of the same size.
        
        Code courtesy Chad Curtis, pulled from L9 Image Proccessing Lecture.
        
        Parameters:
        -----------
        Edge Detected Image: 2D array
        Output of an edge detection program/canny edge detection algorithm.
        Image Binary: 2D array
        Bitmap/binary image (should only contain 1's and 0's.
        segment_properties: Pandas dataframe, four columns
        Example:
        X               Y               Area
        0       436.629412      436.629412      170.0
        1       55.029162       55.029162       4835.0
        2       662.983593      662.983593      1219.0
        ...     ...             ...             ...
    
    Code courtesy Chad Curtis, pulled from L9 Image Proccessing Lecture"""
    
    props = regionprops(segmented_image, intensity_image=binary)
    x = y = area = perimeter = intensity = np.zeros(len(props))

    index_i = 0

    for index_j in props:
        x[index_i] = index_j.centroid[0]
        y[index_i] = index_j.centroid[1]
        area[index_i] = index_j.area
        
        index_i = index_i + 1
    
    segment_properties = pd.DataFrame({'X': x, 'Y': y, 'Area': area})

    return segment_properties

def imageseg(Cont_Image):
    """imageseg('Image Name')
        
    This program takes an image that has been pre-proccessed by an edge finding script as its sole input, segments it, and spits out a segmented image file and a pandas dataframe of individual particle positions.
    
    This function works by creating a binary of an image that has been run through edge detection software, then finding the center of those particles through an Euclidean Distance function.  This was chosen over the typical watershed iterative erosion method because of its increased control in finding the center of particles, allowing for greater detection of overlapped and small particles.
    
    Methodology ideas pulled from the SciKit Image example pages (https://scikit-image.org) as well as the Open CV example pages (https://opencv.org) and Adrian Rosebrock's blog (https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/)."""

    proccessedImage = np.array(Cont_Image, dtype=np.uint8)
    kernel = np.ones((5,6), np.uint8)
    opening = cv2.morphologyEx(Cont_Image, cv2.MORPH_OPEN, kernel)
    canny = cv2.Canny(opening,100,150,3,L2gradient=True)
    
    ret, binary = cv2.threshold(Cont_Image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    distTransform = ndimage.distance_transform_bf(binary)
    localMax = peak_local_max(distTransform, indices=False, min_distance=20,labels=binary)
    label = ndimage.label(localMax)[0]
    segments = watershed(-distTransform, label, mask=binary)

    segment_locations = segmentparser(segments, binary)

    return segments, segment_locations
