import cv2
import matplotlib.pyplot as plt
import numpy as np
import circle
def test_get_circles():
	""" Test function for get_circle function"""
	img = cv2.imread("sem_images/Opal_Tecopa_near_gem.jpg",0) 
	img = cv2.medianBlur(img,5)
	circles = circle.get_circles(img,3,20,150,50,0,30)
	assert type(circles) == tuple
	return