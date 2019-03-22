import cv2
import numpy as np
import pandas as pd
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
    """
    
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
