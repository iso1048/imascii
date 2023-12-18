import os
import math
import string
import argparse
import numpy as np 
from PIL import Image
import functions as func

if __name__ == "__main__":

    #==============================
    # argument parser

    parser = argparse.ArgumentParser()
    parser.add_argument("image",
        help="path to image",
        type=func.is_file)
    parser.add_argument("-wt", "--width",
        help="Value to modify width. A value of 0-1 is used as a ratio\
            to calculate the resized image width. Values >1 are used as\
            the number of pixels in the resized image width. E.g. -w 0.5\
            would halve the width of the image, and -w 30 would set the\
            image width as 30 pixels. By default, the image will undergo\
            proportional resizing so that its width fits within the width\
            of the terminal window.",
        type=float)
    parser.add_argument("-ht", "--height",
        help="Value to modify height. A value of 0-1 is used as a ratio\
            to calculate the resized image height. Values >1 are used as\
            the number of pixels in the resized image height. E.g. -h 0.5\
            would halve the height of the image, and -h 30 would set the\
            image height as 30 pixels.",
        type=float)
    parser.add_argument("-d", "--distort",
        help="When passed, causes the image to undergo non-proportional\
            resizing (i.e. only the specified dimension is changed) if\
            -wt or -ht are also passed. If both -wt and -ht are passed,\
            the image will always undergo non-proportional resizing.\
            Defaults to False.",
        action="store_true")
    parser.add_argument("-t", "--threshold",
        help="Integer to use as the threshold value for converting a\
            greyscale pixel (of value in the range 0 to 255) to either\
            black or white. Defaults to 127.",
        type=func.int_8bit,
        default=127)
    parser.add_argument("-c", "--char_set",
        help="Characters to use to generate the ascii image. Defaults to\
            \"0QO\".",
        default="0QO")
    parser.add_argument("-r", "--random",
        help="Selects characters from the character set at random when\
            generating the ascii image. By default, characters are\
            selected based on the order they appear in in the given\
            character set, and the characters are repeated in that order.",
        action="store_true")
    parser.add_argument("-s", "--save",
        help="Filename to save ascii image to (as .txt file)")

    args = parser.parse_args()

    #==============================
    # open + resize image

    raw_img = Image.open(args.image).convert('RGB')
    resized_img = raw_img.copy()

    if not args.height and not args.width:
        # resize to fit width into terminal window by default
        terminal_width = os.get_terminal_size().columns
        new_width = math.floor(terminal_width / 10) * 10
        resized_img = func.resize_img(resized_img, "width", new_width, not args.distort)

    else:
        if args.height and args.width:
            args.distort = True
        if args.height:
            resized_img = func.resize_img(resized_img, "height", args.height, not args.distort)
        if args.width:
            resized_img = func.resize_img(resized_img, "width", args.width, not args.distort)

    print("",
        f"original image: width={raw_img.size[0]}, height={raw_img.size[1]}",
        f"resized image: width={resized_img.size[0]}, height={resized_img.size[1]}",
        sep="\n")
    
    try:
        print(f"terminal width={terminal_width}")
    except:
        pass

    #==============================
    # convert to black&white image

    img_arr = np.asarray(resized_img)
    bw_img_arr = func.to_blackwhite(img_arr, args.threshold)

    # uncomment lines below to display black&white image
    # bw_img = Image.fromarray(bw_img_arr)
    # bw_img.show()

    #==============================
    # generate ascii image ± save

    ascii_img = func.make_ascii_img(bw_img_arr, args.char_set, args.random)

    print(ascii_img)

    if args.save:
        outfile_name = args.save + ".txt"
        with open(outfile_name, "w") as f:
            f.write(ascii_img)
        
        print("\n --- file saved ---")



