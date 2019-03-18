import Shape_fitting

canny_image = cv2.imread("nanoBALLS/SEM_Images/canny_image")
mean_contour_Area = 1200
def test_Get_Ellipse(canny_image,mean_contour_Area):
    """A funtion that carries the unittests for Get_Ellipse function"""
    assert type(Shape_fitting.Get_Ellipse(canny_image,mean_contour_Area))==list,"Expecting a list"
    major_axis=Shape_fitting.Get_Ellipse(canny_image,mean_contour_Area)[0]
    minor_axis=Shape_fitting.Get_Ellipse(canny_image,mean_contour_Area)[1]
    assert len(major_axis)==len(minor_axis),"length of the both the lists is not same"
    for i in range(len(major_axis)):
        assert major_axis[i]>minor_axis[i],"major axis must be greater tha minor axis"
        assert type([major_axis[i],minor_axis[i]])==float,"The objects in the list must be float"
    return

def test_Predict_Shape():
    """A funtion that carries the unittests for Predict_Shape function"""
    assert type(Shape_fitting.Predict_Shape(major_axis,minor_axis))==int,"Number no circles or ellipse must be an int"
    assert Shape_fitting.Predict_Shape(major_axis,minor_axis)[0]+Shape_fitting.Predict_Shape(major_axis,minor_axis)[1]==len(major_axis),
    	 	"All the elements must be classified as circle or ellipse "
    return
