import cv2
import numpy as np
import pandas as pd
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
