import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import PIL.Image as Image

from matplotlib import pyplot as plt
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
from skimage.measure import label
from skimage.measure import regionprops
from nanoballs import nanoballsfuncs as nan


def output(name, mag=0, Alpha=1.7, Beta=0, dp=3, minDist=20, para1=150, para2=50, minradius=0, maxradius=30, mean_contour_Area=1200):

    imageInput = cv2.imread(name, 0)
    x = cv2.imread(name, 0)
    convFactor = nan.getConv(name, mag)
    canny2, img2 = nan.adjustment(name, Alpha, Beta)
    copy_canny = canny2
    circle_radii, circ_img = nan.get_circles(
        imageInput, dp, minDist, para1, para2, minradius, maxradius)
    major_axis, minor_axis = nan.get_ellipse(canny2, mean_contour_Area)
    segments, segment_locations, opening, canny = nan.imageseg(canny2)
    comp = nan.compare(major_axis, minor_axis)
    circular_particle, ellipsoidal_particle = nan.predict_shape(
        major_axis, minor_axis)

    meanRadius = round(np.mean(circle_radii) * convFactor)
    stdRadius = round(np.std(circle_radii) * convFactor)
    maxRadius = round(np.max(circle_radii) * convFactor)
    minRadius = round(np.min(circle_radii) * convFactor)
    circleCount = np.size(major_axis)
    ellipseCount = ellipsoidal_particle

    data = [['Mean', meanRadius], ['Standard Deviation', stdRadius], ['Maximum', maxRadius], [
        'Minimum', minRadius], ['Circle Count', circleCount], ['Ellipse Count', ellipseCount]]
    outputDF = pd.DataFrame(data, columns=['Statistic', 'Value'])
    display(outputDF)

    fig, ax = plt.subplots(2, 2, figsize=(10, 10))
    ax[0, 0].imshow(x, cmap='gray')  # Image input
    ax[0, 0].set_title("Input Image")
    ax[1, 0].imshow(segments)  # Segmentation type 2
    ax[1, 0].set_title("Image Segmentation")
    ax[0, 1].imshow(circ_img, cmap='gray')  # Circle Fit image
    ax[0, 1].set_title("Circle Detection")
    ax[1, 1].imshow(canny2)  # Ellipse Fit image
    ax[1, 1].set_title("Ellipse fit")
    return