import os
import cv2
import pytesseract
import numpy as np
import pandas as pd
import PIL.Image as Image
from matplotlib import pyplot as plt


def getMag(name):
	img = cv2.imread(name)  # Image to be analyzed

	while True:
		try:
			pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
			# Crops image to magn. details, increases reliability of OCR
			magCrop = img[443:465, 160:243]
			# Inverts colors, easier for OCR software to read
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
				print("Using user input...")
				print(
					"If you did not manually enter this magnification level, results will likely be wrong!")
				break
	return mag


def getConv(name):
	mag = getMag(name)

	conv = pd.read_csv('ConversionFactors.csv')  # Tabulated conversion factors
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
