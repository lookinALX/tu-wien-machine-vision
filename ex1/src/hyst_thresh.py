#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Hysteresis thresholding

Author: FILL IN
MatrNr: FILL IN
"""

import cv2
import numpy as np


def hyst_thresh(edges_in: np.array, low: float, high: float) -> np.array:
    """ Apply hysteresis thresholding.

      Apply hysteresis thresholding to return the edges as a binary image. All
      eight-connected pixels with value > low are considered a valid edge if at
      least one pixel has a value > high.

      Perform threshold comparisons on the floating-point input values without
      normalizing them again. For cv2.connectedComponents, use an np.uint8 mask
      with zero-valued background and nonzero foreground pixels.

      If no pixels have a value > high, return an all-zero image.
      Do not modify the input array.

    :param edges_in: Edge strength of the image in range [0.,1.]
    :type edges_in: np.array with shape (height, width) with dtype = np.float32 and values in the range [0., 1.]

    :param low: Threshold which a pixel's value must exceed to belong to an edge
    :type low: float in range [0., 1.]

    :param high: Threshold which at least one pixel in a connected edge must exceed
    :type high: float in range [0., 1.]

    :return: Binary edge image
    :rtype: np.array with shape (height, width) with dtype = np.float32 and values either 0 or 1
    """
    ######################################################
    # Write your own code here
    bitwise_img = edges_in.copy()  # Replace this line



    ######################################################
    return bitwise_img
