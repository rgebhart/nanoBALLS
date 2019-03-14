![alt](https://i.imgur.com/bVjtiMe.jpg)  
## Package for SEM Image and Particle Analysis
This package is a tool to help analyze and learn the characteristics of particles captured in an SEM image. It takes an SEM image (supported file types listed [here](https://docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html#imread)), and cleans it up using a variety of noise-reduction and edge-enhancement processes. It then analyzes each image, detects the edges of each particle, and then returns particle characteristics such as the average size, size range, count, and a distribution plot of the particles, as well as a circle-fit image for further use and processing. This package could be improved upon by adding more in-depth analysis of the particles, including roughness

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
"List all of the .py files and a one sentence description of each. More details should be included in the other README"

### Project Organization (Clean this section before submission)
"These are the files/__folders__ that will be visible when you go to our github url"
* __Main Folder__: Contains all necessary .py files 
* __Jupyter Notebooks__: All old .ipynb files (not used for anything, just as record keeping)
* __Documentation__: Presentation slides, poster files, images, use cases, etc.
* __Examples__: (maybe? filled out .ipynb notebook or something like that)
* Main File: What the user interacts with (.ipynb? .py? GUI?)
* LICENSE
* README

---

### Acknowledgements (Clean this section before submission)
Beck, TAs, etc.
