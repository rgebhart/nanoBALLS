import cv2
import matplotlib.pyplot as plt
import numpy as np
def get_circles(img,dp,minDist,para1,para2,minradius,maxradius):
    """ The following functions takes in the gray scale image and returns the radius of the circle and the image.
    Arguments:
    image: Gray scale image input
    dp: Inverse ratio of the accumulator resolution to the image resolution.
    minDist: Minimum distance between the centers of the detected circles.
    para1 : It is the higher threshold of the two passed to the Canny edge 
    para2 : It is the accumulator threshold for the circle centers at the detection stage.
    minRadius : Minimum circle radius.
    maxRadius : Maximum circle radius. """
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,dp,minDist,
                            param1=para1,param2=para2,minRadius=minradius,maxRadius=maxradius)
    circles = np.uint16(np.around(circles))
    circle_radii = circles[0][:,2]
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    return (circle_radii,img)
