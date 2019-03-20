import cv2
import matplotlib.pyplot as plt
import numpy as np
def GetCircles(img,dp,minDist,para1,para2,minRadius,maxradius):
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,dp,minDist,
                            param1=para1,param2=para2,minRadius=minRadius,maxRadius=maxradius)
    circles = np.uint16(np.around(circles))
    circle_radii = circles[0][:,2]
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    return (circle_radii,img)
