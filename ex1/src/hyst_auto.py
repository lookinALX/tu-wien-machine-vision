#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Automatic hysteresis thresholding

Author: FILL IN
MatrNr: FILL IN
"""

import cv2
import numpy as np

from hyst_thresh import hyst_thresh


def hyst_thresh_auto(edges_in: np.array, low_prop: float, high_prop: float) -> np.array:
    """ Apply automatic hysteresis thresholding.

    Apply automatic hysteresis thresholding by automatically choosing the high
    and low thresholds of standard hysteresis thresholding. low_prop is the
    proportion of nonzero edge pixels remaining after non-maximum suppression
    which should lie above the low threshold, and high_prop is the proportion
    above the high threshold.

    Exclude zero-valued background pixels when calculating the thresholds.
    Small differences due to percentile interpolation or rounding are acceptable.
    Pass the original, spatially arranged input image to hyst_thresh without
    normalizing it again. If there are no edge pixels, return an all-zero image.
    Do not modify the input array.

    :param edges_in: Edge strength of the image in range [0., 1.]
    :type edges_in: np.array with shape (height, width) with dtype = np.float32 and values in the range [0., 1.]

    :param low_prop: Proportion of nonzero edge pixels which should lie above the low threshold
    :type low_prop: float in range [0., 1.]

    :param high_prop: Proportion of nonzero edge pixels which should lie above the high threshold
    :type high_prop: float in range [0., 1.]

    :return: Binary edge image
    :rtype: np.array with shape (height, width) with dtype = np.float32 and values either 0 or 1
    """
    ######################################################
    # Write your own code here
    hyst_out = edges_in.copy()  # Replace this line



    ######################################################
    return hyst_out
