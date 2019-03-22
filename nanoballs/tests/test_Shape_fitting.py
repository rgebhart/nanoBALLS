from nanoballs import Shape_fitting
import cv2
import numpy as np
img = cv2.imread("C:/Users/Omkar/Desktop/nanoBALLS/sem_images/Opal_Tecopa_near_gem")
img = np.array(img, dtype=np.uint8)
kernel = np.ones((5,5), np.uint8)
alpha = 1.7 # Simple contrast control
beta = 0    # Simple brightness control
img2 = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
canny_image = cv2.Canny(opening,100,150,3,L2gradient=True)
mean_contour_Area = 1200
x=(Shape_fitting.get_ellipse(canny_image,mean_contour_Area))
major_axis=x[0]
minor_axis=x[1]

def test_get_ellipse():
    """A funtion that carries the unittests for Get_Ellipse function """
    assert type(Shape_fitting.get_ellipse(canny_image,mean_contour_Area))==tuple,"Expecting a tuple"
    major_axis=x[0]
    minor_axis=x[1]
    assert len(major_axis)==len(minor_axis),"length of the both the lists is not same"
    for i in range(len(major_axis)):
        assert major_axis[i]>minor_axis[i],"major axis must be greater tha minor axis"
    return

def test_predict_shape():
    """A funtion that carries the unittests for Predict_Shape function """
    assert type(Shape_fitting.predict_shape(major_axis,minor_axis))==tuple,"Expecting a tuple"
    assert Shape_fitting.predict_shape(major_axis,minor_axis)[0]+Shape_fitting.predict_shape(major_axis,minor_axis)[1]==len(major_axis),"All the elements must be classified as circle or ellipse "
    return
