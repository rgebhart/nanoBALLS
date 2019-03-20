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
_Add more here probably_  
This package could be improved upon by adding more in-depth analysis of the particles, including roughness.

---

### Acknowledgements (Clean this section before submission)
Team nanoBALLS wishes to thank David Beck, Chad Curtis, and the rest of the teaching staff for guiding us through this proccess and teaching us enough to get us started.
We also wish to thank Dr. Erika Buckle for collecting these images, the UW MAF for providing equipment and facility management, and Prof. Jim Pfaendtner for the project conception.
Lastly, we wish to extend our gratitutudes to Professors Drobny, Eric Stuve, Samson Jenekhe, and Arka Majumdar for allowing us to participate in this class.
