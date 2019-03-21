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
    """Docstring.
    
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
    
    This function works by creating a binary of an image that has been run through edge detection software, then finding the center of those particles through an Euclidean Distance function.  This was chosen over the typical watershed iterative erosion method because of its increased control in finding the center of particles, allowing for greater detection of overlapped and small particles.  """

    proccessedImage = np.array(Cont_Image, dtype=np.uint8)
    
    ret, binary = cv2.threshold(Cont_Image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    distTransform = ndimage.distance_transform_bf(binary)
    localMax = peak_local_max(distTransform, indices=False, min_distance=20,labels=binary)
    label = ndimage.label(localMax)[0]
    segments = watershed(-distTransform, label, mask=binary)

    segment_locations = segmentparser(segments, binary)

    return segments, segment_locations
