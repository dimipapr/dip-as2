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
    

filepath = "images/im5.jpg"
img_bgr = cv2.imread(filepath,cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
img_gs = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gs,(31,31),sigmaX=0,sigmaY=0)
img_sobel = cv2.Sobel(img_blur,ddepth=-1,dx=1,dy=1,ksize=5)
img_canny = cv2.Canny(img_blur, threshold1=0,threshold2=50)
plot.figure()
plot.imshow(img_gs,cmap='gray')
plot.figure()
plot.imshow(img_sobel,cmap='gray')
plot.figure()
plot.imshow(img_canny,cmap='gray')
plot.show()