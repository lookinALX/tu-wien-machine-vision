#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Edge detection with the Sobel filter

Author: FILL IN
MatrNr: FILL IN
"""

import cv2
import numpy as np


def sobel(img: np.array) -> (np.array, np.array):
    """ Apply the Sobel filter to the input image and return the gradient and the orientation.

    Normalize the gradient magnitudes by dividing by their maximum. If the maximum
    is zero, return an all-zero gradient array. Do not modify the input image.

    :param img: Grayscale input image
    :type img: np.array with shape (height, width) with dtype = np.float32 and values in the range [0., 1.]
    :return: (gradient, orientation): gradient: the normalized edge strength of the image in range [0.,1.],
                                      orientation: angle of gradient in range [-np.pi, np.pi]
    :rtype: Two np.arrays with shape (height, width) and dtype = np.float32
    """
    ######################################################
    # Write your own code here
    gradient = img.copy()     # Replace this line
    orientation = img.copy()  # Replace this line



    ######################################################
    return gradient, orientation
