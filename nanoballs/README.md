### Packages Included
* __circle.py__: Finds circles using the Hough transform and draws the circle's center and edge
* __contrast_adj.py__: Adjusts brightness and contrast of image to improve edge-detection 
* __convert.py__: Determines most efficient way (OCR, file name, user input) to get the magnification level, returns pixel length to nanometer conversion factor
* __imageseg.py__: Takes pre-processed image, returns segmented image and particle-center coordinates
* __segmentparser.py__: Iterates through the segmented image, calculates image coordinates and area
* __shape_fitting.py__: Fits ellipses to particles, determines the major and minor axis, predicts whether each particle is a circle or an ellipse, and then returns a distribution plot of the shape types
