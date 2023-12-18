# imascii

Script for converting an image to an ascii representation. 

```
(venv) ...\imascii> python main.py -h

usage: main.py [-h] [-wt WIDTH] [-ht HEIGHT] [-d] [-t THRESHOLD] [-c CHAR_SET] [-r] [-s SAVE] image

positional arguments:
  image                 path to image

options:
  -h, --help            show this help message and exit
  -wt WIDTH, --width WIDTH
                        Value to modify width. A value of 0-1 is used as a ratio to calculate the resized image width. Values >1 are used  
                        as the number of pixels in the resized image width. E.g. -w 0.5 would halve the width of the image, and -w 30      
                        would set the image width as 30 pixels. By default, the image will undergo proportional resizing so that its       
                        width fits within the width of the terminal window.
  -ht HEIGHT, --height HEIGHT
                        Value to modify height. A value of 0-1 is used as a ratio to calculate the resized image height. Values >1 are     
                        used as the number of pixels in the resized image height. E.g. -h 0.5 would halve the height of the image, and -h  
                        30 would set the image height as 30 pixels.
  -d, --distort         When passed, causes the image to undergo non-proportional resizing (i.e. only the specified dimension is changed)  
                        if -wt or -ht are also passed. If both -wt and -ht are passed, the image will always undergo non-proportional      
                        resizing. Defaults to False.
  -t THRESHOLD, --threshold THRESHOLD
                        Integer to use as the threshold value for converting a greyscale pixel (of value in the range 0 to 255) to either  
                        black or white. Defaults to 127.
  -c CHAR_SET, --char_set CHAR_SET
                        Characters to use to generate the ascii image. Defaults to "0QO".
  -r, --random          Selects characters from the character set at random when generating the ascii image. By default, characters are    
                        selected based on the order they appear in in the given character set, and the characters are repeated in that     
                        order.
  -s SAVE, --save SAVE  Filename to save ascii image to (as .txt file)
```

