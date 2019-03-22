![alt](https://i.imgur.com/5IlGL9R.jpg)  
## Package for SEM Image and Particle Analysis
This package is a tool to help analyze and learn the characteristics of particles captured in an SEM image. It takes an SEM image (supported file types listed [here](https://docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html#imread)), and cleans it up using a variety of noise-reduction and edge-enhancement processes. It then analyzes the image, detects the edges of each particle, and returns particle characteristics such as the average size, size range, count, and a distribution plot of the particles, as well as a circle-fit image for further use and processing. 

---

### How to Install
1. `pip install nanoballs`
2. Import necessary packages

### How to Use
Simply download the `nanoballs_UI.ipynb` and follow the instructions!

### Software Dependencies
* __Python3.6__
* __Packages__: argparse, Matplotlib, NumPy, OpenCV, pandas, scikit-learn, SciPy
    * Optional: nose (testing)
* __Tesseract OCR__: Image-to-text converter, available [here](https://pypi.org/project/pytesseract/)
    * Not necessary for use of the code, but helps expedite analysis of large sets of images
    
---

### Project Organization
```
documentation/ (Presentation slides, use cases, etc.)
    Poster/
nanoballs/ (Main package folder, contains all necessary .py files)
    tests/ (Tests folder, contains files for unit testing)
        __init__.py
        README.md
    __init__.py
    nanoballsfuncs.py
    output.py
    README.md
notebooks/ (All .ipynb files, contain helpful markdown comments)
sem_images/ (Extra SEM images, can be used for testing or optimization)
nanoballs_UI.ipynb
setup.py
LICENSE.txt
README.md

```

---

### Example Usage
|     |     |     |
|:---:|:---:|:---:|
| (1) Image Input and Pre-Processing | ![](https://imgur.com/iYQr9SA.jpg) | ![](https://imgur.com/q0LIoAy.jpg) |
| (2) Segmentation | ![](https://i.imgur.com/xNhUkoP.jpg) | ![](https://imgur.com/qXAATw7.jpg) |
| (3) Shape Fitting | ![](https://imgur.com/ha1j9Ut.jpg) | ![](https://imgur.com/genut41.jpg) |
| (4) Data Output | ![](https://imgur.com/RTWHMLR.jpg) | ![](https://imgur.com/T8zl76j.jpg) |

(_Statistics refer to the particle radius unless otherwise noted_) 

---

### Improvements 
This package is a work in progress, and much improvement could be made upon each step of the process. Better automation of the image contrast and brightness adjustments could go a long way, as could more complicated transforms. Currently a scaling factor is used to optimize the adjustments, but a script that normalizes the spread of the image histogram could afford more uniformity in processing and make this software more robust.

Edge detection could be improved on by stacking edge detection methods, with the hope being that a more contiguous edge would be produced. From there, experimentation with the p algorithm could produce finer edge detection than the built in Watershed algorithms currently available. Integration of the mamba-image package would be necessary to introduce this functionality.

While the Hough Circle Fitting has proven robust in its implementation, the addition of a degree of freedom to try and fit ellipses to the segments has proven difficult. Problems in this implementation could be rooted in how these algorithms work, as well as our understanding of their inputs (logical errors). More work is required to produce a useful end product.

From a stretch goal perspective, this software could also be improved upon by adding more in-depth analysis of the particles, including roughness. Other ideas for improvement include breaking the image down and adjusting the contrast and brightness differently for different tiles within the image to best detect edges, and training a neural network to set these parameters for us.

At the end of the day, though, a major criticism of our work is our lack of scientific benchmarking. While we can visually see whether or not the code seems to be operating as expected and is throwing out a logical visual output, we do not have a good numeric benchmark of how closely these segmentations, circle fits, etc. are representing our data. Development of a means of better benchmarking our results would help drive development of robust code in the future.

---

### Acknowledgements
Team nanoBALLS wishes to thank David Beck, Chad Curtis, and the rest of the teaching staff for guiding us through this process and teaching us enough to get us started.

We also wish to thank Dr. Erika Buckle for collecting these images, the UW MAF for providing equipment and facility management, and Prof. Jim Pfaendtner for the project conception.

Lastly, we wish to extend our gratitude to Professors Drobny, Eric Stuve, Samson Jenekhe, and Arka Majumdar for allowing us to participate in this class.
