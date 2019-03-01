# Use Cases
---
## Use Case 1: Edge Detection
#### CHARACTERISTIC INFORMATION  
__Goal:__ User provides an SEM image to the program, receives edge-detected image as output.  
__Success End Condition:__ User receives image with accurate edges.  
__Failed End Condition:__ User receives inaccurate edge detection or no image at all.

#### COMPONENTS
1. GUI asks user to upload an image.
2. Program uses edge detection methods to develop output images.
3. Checks images for accuracy.
4. Returns side-by-side comparison of original image with edge-detected images.

#### EXTENSIONS
1. User inputs a file of incompatible type.
  * Asks user for file of proper type
2. Image accuracy is below threshold.
  * Asks user for cleaner image  
  
---
## Use Case 2: Image Analysis
#### CHARACTERISTIC INFORMATION  
__Goal:__ User receives values of interest from image analysis.  
__Success End Condition:__ User receives values that accurately represent the characteristics of the image.  
__Failed End Condition:__ User receives inaccurate results or no results at all.

#### COMPONENTS
1. GUI asks user if they'd like SEM image characteristics.
2. Program calculates the following characteristics:
  * Average particle size
  * Particle size distribution
  * Measure of how spherical or elliptical a particle is
  * Particle roughness
3. Checks values for accuracy.
4. Returns table of values to the user.

#### EXTENSIONS
1. Value accuracy is below threshold.
  * Asks user for cleaner image.
  * Returns values that are above threshold.