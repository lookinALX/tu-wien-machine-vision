#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Blur the input image with Gaussian filter kernel

Author: FILL IN
MatrNr: FILL IN
"""

import cv2
import numpy as np

def blur_gauss(img: np.array, sigma: float) -> np.array:
    """ Blur the input image with a Gaussian filter with standard deviation of sigma.

    Construct a two-dimensional Gaussian kernel with standard deviation sigma and
    size 2 * ceil(3 * sigma) + 1 in each dimenstion. Normalize the kernel so its
    values sum to one, then apply it to the input image using cv2.filter2D.
    Do not modify the input image.

    :param img: Grayscale input image
    :type img: np.array with shape (height, width) with dtype = np.float32 and values in the range [0., 1.]

    :param sigma: The standard deviation of the Gaussian kernel
    :type sigma: float

    :return: Blurred image
    :rtype: np.array with shape (height, width) with dtype = np.float32 and values in the range [0.,1.]
    """
    ######################################################
    # Write your own code here
    def gauss(x: int, y: int, sigma: float) -> float:
            return (1/(2*np.pi*sigma**2) * np.exp(-1*(x**2 + y**2)/(2 * sigma ** 2)))
    
    size = int(2 * np.ceil(3 * sigma) + 1)
    filter = np.empty((size, size))

    sum = 0
    center = (size - 1) / 2 
    for idx in np.ndindex(filter.shape):
          x = idx[0] - center
          y = idx[1] - center
          filter[idx] = gauss(x, y, sigma)
          sum += filter[idx]

    filter /= sum

    img_blur = cv2.filter2D(img, ddepth = -1, kernel=filter)

    ######################################################
    return img_blur
