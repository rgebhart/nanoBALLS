![alt](https://i.imgur.com/5IlGL9R.jpg)  
## Package for SEM Image and Particle Analysis
This package is a tool to help analyze and learn the characteristics of particles captured in an SEM image. It takes an SEM image (supported file types listed [here](https://docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html#imread)), and cleans it up using a variety of noise-reduction and edge-enhancement processes. It then analyzes the image, detects the edges of each particle, and then returns particle characteristics such as the average size, size range, count, and a distribution plot of the particles, as well as a circle-fit image for further use and processing. 

---

### How to Install
1. Use `git clone` to copy the repository
2. Import necessary packages

### Software Dependencies
* __Python3.6__
* __Packages__: argparse, Matplotlib, NumPy, OpenCV, pandas, scikit-learn, SciPy
* __Tesseract OCR__
    * Not necessary for use of the code, but helps expedite analysis of large sets of images
---

### Packages Included
_List all of the .py files and a one sentence.phrase description of each. More details of each function should be included in the other README_
* __convert.py__: Takes SEM image as input, returns pixel length to nanometer conversion factor
* __segmentparser.py__: Iterates through a segmented image, pulling coordinates and areas of each segment, and returning them to the user in a pandas dataframe
* __imageseg.py__: Takes an edge detected image file as an input, and uses the watershed algorithm to segment the image

### Project Organization (Clean this section before submission)
These are the folders contained in our repository
* __nanoBALLS__: Main package folder, contains all necessary .py files 
    * tests: Tests folder, contains files for unit testing
* __Notebooks__: All .ipynb files, contain helpful markdown comments
* __Documentation__: Presentation slides, use cases, etc.
    * Poster: Files for poster
* __Examples__: Notebook files, already run with output
* __SEM_Images__: Extra SEM images, can be used for testing or optimization
* LICENSE
* README

---

### Example Usage
_Example of image input, image output, and particle characteristics_

#### Image Input: _SEM image to be analyzed_
#### Image Output: _Circle-fit SEM image_
#### Data Output: _Particle characteristics of SEM image_

### Improvements 
This package is a work in progress, and much improvement could be made upon each step of the proccess.  Better automization of the image contrast and brightness adjustments could go a long way, as could more complicated transforms.  Currently a scaling factor is used to optimize the adjustments, but a script that normalizes the spread of the image histogram could afford more uniformity in proccessing and make this software more robust.  

Edge detection could be improved on by stacking edge detection methods, with the hope being that a more contiguous edge would be produced.  From there, experimentation with the p algorithm could produce finer edge detection than the built in Watershed algorithms currently available.  Integration of the mamba-image package would be neccissary to introduct this functionality.  

While the Hough Circle Fitting has proven robust in its implementation, the addition of a degree of freedom to try and fit elipses to the segments has proven difficult.  Problems in this implementation could be rooted in how these algorithms work, as well as our understanding of their inputs (logical errors).  More work is required to produce a useful end product.

From a stretch goal perspective, this software could also be improved upon by adding more in-depth analysis of the particles, including roughness.  Other ideas for improvement include breaking the image down and adjusting the contrast and brightness differently for different tiles within the image to best detect edges, and training a neural network to set these parameters for us.

At the end of the day, though, a major cricicism of our work is our lack of scientific benchmarking.  While we can visually see whether or not the code seems to be operating as expected and is throwing out a logical visual output, we do not have a good numeric benchmark of how closely these segmentations, circle fits, etc. are representing our data.  Development of a means of better benchmarking our results would help drive development of robust code in the future.

---

### Acknowledgements (Clean this section before submission)
Team nanoBALLS wishes to thank David Beck, Chad Curtis, and the rest of the teaching staff for guiding us through this proccess and teaching us enough to get us started.

We also wish to thank Dr. Erika Buckle for collecting these images, the UW MAF for providing equipment and facility management, and Prof. Jim Pfaendtner for the project conception.

Lastly, we wish to extend our gratitutudes to Professors Drobny, Eric Stuve, Samson Jenekhe, and Arka Majumdar for allowing us to participate in this class.
