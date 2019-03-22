import cv2
import matplotlib.pyplot as plt
import numpy as np
from nanoballs import circle
def test_get_circles():
	""" Test function for get_circle function"""
	img = cv2.imread("C:/Users/Omkar/Desktop/nanoBALLS/sem_images/Opal_Tecopa_near_gem.jpg",0) 
	img = cv2.medianBlur(img,5)
	circles = circle.GetCircles(img,3,20,150,50,0,30)
	assert type(circles) == tuple, "Expecting a tuple got something else"
	return