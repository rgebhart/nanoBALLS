def Adjustment(ImageName, Alpha, Beta):
    # Alphafactor for contrast control
    # Beta for brightness control

    import numpy as np
    import cv2

    img = cv2.imread(ImageName)
    img = np.array(img, dtype=np.uint8)
    img2 = cv2.convertScaleAbs(img, alpha=Alpha, beta=Beta)
    kernel = np.ones((5, 5), np.uint8)
    opening2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
    canny2 = cv2.Canny(opening2, 100, 150, 3, L2gradient=True)

    return canny2