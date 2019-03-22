### Packages Included
* __nanoballsfuncs.py__:
  * __adjustment__: Adjusts brightness and contrast of image to improve edge-detection
  * __compare__: Gives the plot of major axis vs minor axis of the ellipse and compares it with the circle
  * __get_circles__: Finds circles using the Hough transform and draws the circle's center and edge
  * __getConv__: Returns pixel length to nanometer conversion factor
  * __get_ellipse__: Returns the major and the minor axis of the ellipse.
  * __getMag__: Determines most efficient way (OCR, file name, user input) to get the magnification level
  * __imageseg__: Takes pre-processed image, returns segmented image and particle-center coordinates
  * __predict_shape__: Predicts whether the object detected is circle or ellispeIt is the short axis of the ellipse
  * __segmentparser__: Iterates through the segmented image, calculates image coordinates and area
  
* __output.py__:
  * __output__: Takes user input, runs through `nanoballsfuncs`, and returns images, plots, and data
