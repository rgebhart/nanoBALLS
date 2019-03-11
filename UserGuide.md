### Project Subcategories
* Image Blurring
* Image Segmentation/Edge Detection
* Circle Fitting
* Unit Conversions
---
Sidenote: Should figure out what order these functions are called. We need to know how the user will be interacting with the code, what type of input they will be giving (image path, single image upload, folder/zip upload, etc.), and then how each function output will be passed to the next function

---

### Image Blurring
#### Goal: Improve efficiency of edge detection functions
__Potential Unit Tests__:
* Check for correct file type (assuming this is where images are uploaded)
* 

### Image Segmentation/Edge Detection
#### Goal: Return edge-detected image using output from image blurring
__Potential Unit Tests__:
* 
* 

### Circle Fitting
#### Goal: Fit circles to edges, returns number, size range/average
__Potential Unit Tests__:
* 
* 

### Unit Conversions
#### Goal: Take pixel length values from circle fitting and convert to nanoscale
__Potential Unit Tests__:
* Check that OCR-detected magnification level is an integer
* Check that OCR detects a magnification value that is tabulated
    * If not, ask user for different magnification level
* Check that pixel length from circle fitting is an integer or list or whatever we want it to be 
