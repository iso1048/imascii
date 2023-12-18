
import os
import random
import numpy as np
from PIL import Image

def is_file(path):
    if os.path.exists(path):
        return path
    else:
        raise TypeError

def int_8bit(val):
    if 0 <= int(val) <= 255:
        return int(val)
    else:
        raise ValueError

def resize_img_ratio(img, dim, resize_ratio, scale=True):
    """
    Resizes img in the given dimension based on the resize_ratio.
    If scale is True, the other dimension is scaled by the same
    ratio, otherwise it remains unchanged.
    @param  img (PIL Image)
    @param  dim (str)
        "width" or "height"
    @param  resize_ratio (float)
        in range 0-1
    @param  scale (bool)
    @return PIL Image
    """
    img_width, img_height = img.size

    if dim == "width":
        new_width = int(img_width * resize_ratio)
        new_height = int(img_height * resize_ratio) if scale else img_height

    elif dim == "height":
        new_width = int(img_width * resize_ratio) if scale else img_width
        new_height = int(img_height * resize_ratio)
    
    else:
        raise TypeError
    
    return img.resize((new_width, new_height))

def resize_img_pixels(img, dim, num_pixels, scale=True):
    """
    Resizes img in the given dimension to the given number of pixels.
    @param  num_pixels (int)
        number of pixels to set the given dimension to

    see docstring of resize_img_ratio 
    """

    img_width, img_height = img.size
    px = int(num_pixels)
    if dim == "width":
        resize_ratio = px / img_width
    elif dim == "height":
        resize_ratio = px / img_height
    else:
        raise TypeError
    
    return resize_img_ratio(img, dim, resize_ratio, scale)

def resize_img(img, dim, resize_val, scale=True):
    if 0 <= resize_val <= 1:
        return resize_img_ratio(img, dim, resize_val, scale)
    else:
        return resize_img_pixels(img, dim, resize_val, scale)

def to_greyscale(img_arr):
    """
    converts colour image np array to greyscale image array according to
    the formula: 0.299∙R + 0.587∙Green + 0.114∙Blue

    @param  img_arr (np.array)
        shape (x, y, 3), where for axis 2 channels, 0=R, 1=G, and 2=B
    @return np.array
    """

    R_mod = img_arr[:,:,0] * 0.299
    G_mod = img_arr[:,:,1] * 0.587
    B_mod = img_arr[:,:,2] * 0.114

    return R_mod + G_mod + B_mod

def to_blackwhite(img_arr, threshold=127):
    """
    convert colour image np array to black&white image np array
    """
    gs_arr = to_greyscale(img_arr)
    return np.where(gs_arr > threshold, 255, 0)

def make_ascii_img(bw_img_arr, char_set, random_selection):
    """
    Generates ascii image from the black and white image array
    """

    ascii_img = ""
    h, w = bw_img_arr.shape

    for i in range(w*h):

        row, col = i//w, i%w
        if bw_img_arr[row][col] == 255:
            index_into_charset = i%len(char_set)
            ascii_img += random.choice(char_set) if random_selection else char_set[index_into_charset]
        else:
            ascii_img += " "

        if col == w-1:
            ascii_img += "\n"

    return ascii_img
