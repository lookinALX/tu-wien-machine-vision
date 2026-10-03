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
    sobel_x = np.array([
        (-1, 0, 1), 
        (-2, 0, 2), 
        (-1, 0, 1)
    ])
    sobel_y = np.array([
        (-1, -2, -1), 
        (0, 0, 0), 
        (1, 2, 1)
    ])

    gX = cv2.filter2D(img, ddepth=-1, kernel=sobel_x)
    gY = cv2.filter2D(img, ddepth=-1, kernel=sobel_y)

    orientation = np.atan2(gY, gX)
    gradient = np.sqrt(gX**2 + gY**2)
    if np.max(gradient) != 0:
        gradient /= np.max(gradient)

    ######################################################
    return gradient, orientation



if __name__ == "__main__":
    from helper_functions import *
    from pathlib import Path
    from blur_gauss import blur_gauss

    current_path = Path(__file__).parent
    img_gray = cv2.imread(str(current_path.joinpath("image/circle.jpg")), cv2.IMREAD_GRAYSCALE)

    img_gray = img_gray.astype(np.float32) / 255.
    show_image(img_gray, "Original Image", save_image=False, use_matplotlib=False)
    
    sigma = 3  # Change this value
    img_blur = blur_gauss(img_gray, sigma)
    show_image(img_blur, "Blurred Image", save_image=False, use_matplotlib=False)

    gradients, orientations = sobel(img_blur)
    orientations_color = cv2.applyColorMap(np.uint8((orientations.copy() + np.pi) / (2 * np.pi) * 255),
                                               cv2.COLORMAP_RAINBOW)
    orientations_color = orientations_color.astype(np.float32) / 255.
    gradient_img = np.append(cv2.cvtColor(gradients, cv2.COLOR_GRAY2BGR), orientations_color, axis=1)
    show_image(gradient_img, "Gradients", save_image=False, use_matplotlib=False)
    
    
