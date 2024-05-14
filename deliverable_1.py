import numpy as np
from matplotlib import pyplot as plot
from typing import Tuple
import cv2

def my_hough_transform(
    img_binary:np.ndarray,
    d_rho: int,
    d_theta: float,
    n: int
)-> Tuple[np.ndarray, np.ndarray, int]:
    """
    Args:
        img_binary (numpy.ndarray): Binary output of edge detector
        d_rho (int):
        d_theta (float):
        n (int) :
    Returns:
        H (numpy.ndarray):
        L (numpy.ndarray):
        res (int):
    """
    pass
    

filepath = "images/im2.jpg"
img = cv2.imread(filepath,cv2.IMREAD_COLOR)
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plot.figure()
plot.imshow(rgb_img)
plot.show()