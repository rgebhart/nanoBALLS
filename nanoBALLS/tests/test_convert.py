#!/usr/bin/env python
# coding: utf-8

# In[49]:


import os
import cv2
import pytesseract
import numpy as np
import pandas as pd
import PIL.Image as Image
from matplotlib import pyplot as plt
import unittest


# In[50]:


def test_getMag():
    img = cv2.imread('Opal_Tecopa_near_gem.jpg')  # Image to be analyzed

    while True:
        try:
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
            # Crops image to magnification details, increases reliability of
            # OCR
            magCrop = img[443:465, 160:243]
            # Inverts colors, black on white text is easier for OCR software to
            # read
            magCropInv = cv2.bitwise_not(magCrop)
            mag = int(pytesseract.image_to_string(Image.fromarray(magCropInv))[
                      :-1])  # Image to text, removes 'x', makes integer
            print("Using tesseract OCR...")
            break
        except:
            try:
                # Splits file name by underscores, stores in list
                spl1 = name.split('_')
                # Selects the last list entry (number.TIF) and splits by
                # period, stores in list
                spl2 = spl1[-1].split('.')
                # Selects the first list entry (number) and converts to integer
                mag = int(spl2[0])
                print("Using file name...")
                break
            except:
                #**********USER INPUT**********
                mag = 35000
                assert isinstance(
                    mag, int), "User-input magnification needs to be an integer"
                print("Using user input...")
                print(
                    "If you did not manually enter this magnification level, results will likely be wrong!")
                break
    return mag


# In[53]:


def test_getConv():
    mag = test_getMag()
    conv = pd.DataFrame([[35000, 157, 2000, 12.7388535], [25000, 111, 2000, 18.01801802], [15000, 167, 5000, 29.94011976], [
                        12000, 133, 5000, 37.59398496], [10000, 111, 5000, 45.04504505], [6500, 15, 10000, 68.96551724]])  # Tabulated conversion factors
    conv.columns = ['Mag', 'Pixels', 'Length [nm]', 'Conversion']
    assert mag in list(
        conv['Mag']), "Magnification level is not tabulated, please use another image"
    # Finds row that matches the magnification value
    row = conv.loc[conv['Mag'] == mag]
    convFactor = row.iloc[0]['Conversion']  # Gets conversion factor from row
    print("Magnification Level: " + str(mag) + "x")
    print("Conversion Factor [nm/pixel]: " + str(convFactor))
    print("-----------------------------------------------------")

    # Radius of a particle in pixels (This number should be coming from
    # another function somewhere I think)
    pixValue = 10
    # Use conversion factor to get particle radius in nanometers
    nmValue = pixValue * convFactor

    print("Length in [nm]:")
    return nmValue


# In[ ]:
