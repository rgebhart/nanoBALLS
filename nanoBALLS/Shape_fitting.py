import cv2
import numpy as np
import matplotlib.pyplot as plt

def Get_Ellipse(canny_image,mean_contour_Area):
"""This function returns the major and the minor axis of the ellipse.
Arguments:
canny_image : The image whose edges are delected
mean_countour_Area : The mean area of the contours found using the image segmentation   """
	th, threshed = cv2.threshold(canny_image, 120, 255, cv2.THRESH_BINARY)
	threshed = cv2.dilate(threshed, None)
	threshed = cv2.erode(threshed, None)
	# Finding the countours of the image
	cnts = cv2.findContours(threshed, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)[-2]
	# Draws the Contours
	cv2.drawContours(canny_image, cnts, -1, (157, 0, 78), 1, cv2.LINE_AA)
	elps=[]
	# Calculating the range of the area 
	Mean_Area = mean_contour_Area
	Lower_Area = Mean_Area - 0.1*Mean_Area
	Higher_Area =  Mean_Area + 0.1*Mean_Area
	for cnt in cnts:
    	if cnt.size in range (100,200)  or  (cv2.contourArea(cnt)) in 
    		range(Lower_Area,Higher_Area):
# Fitting the ellipse    		        
        	Ellipse = cv2.fitEllipse(cnt)
# Adding rllipse to the list
        	elps.append(Ellipse)
        	cv2.ellipse(canny_image, Ellipse, (255, 0, 0), 2, cv2.LINE_AA)
# Getting the major and minor axis of the Ellipse
        axes=[x[1] for x in elps]
        major_axis=[x[1] for x in axes]
        minor_axis=[x[0] for x in axes]
    return(major_axis,minor_axis)

def Predict_Shape(major_axis,minor_axis):
""" This function predicts whether the object detected is circle or ellispeIt is the short axis of the ellipse
	It returns number of circles or the ellipse in the image
Arguments:
major_axis = It is the long axis of the ellipse
minor_axis = It is the short axis of the ellipse	"""     
    circular_particle = 0
	ellipsoidal_particle = 0
	for i in range(len(major_axis)):
    	x=0.1*major_axis[i]+major_axis[i]
    	y=major_axis[i]-0.1*major_axis[i]
    	if minor_axis[i] <= x and minor_axis[i] >= y:  
        	circular_particle +=1
    	else:
         	ellipsoidal_particle +=1
     return(circular_particle,ellipsoidal_particle)


def Compare(major_axis,minor_axis):
""" This function gives the plot of major axis vs minor axis of the ellipse
	and compares it with the circle.
Arguments:
major_axis = It is the long axis of the ellipse
minor_axis = It is the short axis of the ellipse"""
    p=np.array(range(100))
	q=np.array(range(100))
	plt.scatter(major_axis,minor_axis)
	plt.plot(p,q) 
	plt.xlim(0,80)
	plt.ylim(0,80)
	plt.xlabel("Maximum")
	plt.ylabel("Minimum")
	plt.title("Plot of Minimum vs Maximum")
	plt.legend(["Theoretical circle","Predicted Circle"])
	return       	