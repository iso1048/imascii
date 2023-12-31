# imascii

Script for converting an image to an ascii representation. 

```
(venv) ...\imascii> python main.py -h

usage: main.py [-h] [-wt WIDTH] [-ht HEIGHT] [-d] [-t THRESHOLD] [-c CHAR_SET] [-r] [-s SAVE]
               image

positional arguments:
  image                 path to image

options:
  -h, --help            show this help message and exit
  -wt WIDTH, --width WIDTH
                        Value to modify width. A value of 0-1 is used as a ratio to calculate  
                        the resized image width. Values >1 are used as the number of pixels    
                        in the resized image width. E.g. -w 0.5 would halve the width of the   
                        image, and -w 30 would set the image width as 30 pixels. By default,   
                        the image will undergo proportional resizing so that its width fits    
                        within the width of the terminal window.
  -ht HEIGHT, --height HEIGHT
                        Value to modify height. A value of 0-1 is used as a ratio to
                        calculate the resized image height. Values >1 are used as the number   
                        of pixels in the resized image height. E.g. -h 0.5 would halve the     
                        height of the image, and -h 30 would set the image height as 30        
                        pixels.
  -d, --distort         When passed, causes the image to undergo non-proportional resizing     
                        (i.e. only the specified dimension is changed) if -wt or -ht are also  
                        passed. If both -wt and -ht are passed, the image will always undergo  
                        non-proportional resizing. Defaults to False.
  -t THRESHOLD, --threshold THRESHOLD
                        Integer to use as the threshold value for converting a greyscale       
                        pixel (of value in the range 0 to 255) to either black or white.       
                        Defaults to 127.
  -c CHAR_SET, --char_set CHAR_SET
                        Characters to use to generate the ascii image. Defaults to "0QO".      
  -r, --random          Selects characters from the character set at random when generating    
                        the ascii image. By default, characters are selected based on the      
                        order they appear in in the given character set, and the characters    
                        are repeated in that order.
  -s SAVE, --save SAVE  Filename to save ascii image to (as .txt file)
```

## Example

image: /images/card.jpg

Setting width to 80 pixels

```
(venv) ...imascii>python main.py "/images/card.jpg" -wt 80 

original image: width=188, height=269
resized image: width=80, height=114
0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0Q 0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0      QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0 O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q     QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0    O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0Q 0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q     QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0    O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO    QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0 O QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q    0QO0QO QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0Q 0Q 0QO0QO0QO0QO0QO0QO0QO0QO0QO0        0Q    0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0 O0Q 0QO0QO0QO0QO0QO0QO       Q   O0          O0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0 O QO0QO0QO0QO0QO0QO              O0         QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO                        0   QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO                           0  0 O0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO QO QO0QO0QO0QO         0Q       0          O    QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO  O0QO0QO0QO       QO0QO0QO     O0         Q    0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0Q  QO0QO0QO0      QO0QO0QO0QO0               QO0  0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO QO QO0QO0QO     O0QO0QO0QO0QO0                  QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0    O0QO0QO0QO0QO0Q        Q         O0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0Q   O0QO0QO0QO0QO0Q         O0         QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0 O0QO0QO0  0QO0QO0QO0QO0QO    QO0              0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO QO0QO0QO QO0QO0QO0QO0QO0      Q               O0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0Q 0QO0QO0QO0QO0QO0QO0QO0Q                      0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0 O0QO0QO0QO0QO0QO0QO0QO     O0QO0Q          0 O0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0Q    0QO0QO  O0QO0Q     Q 0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0QO    QO0QO       QO0Q   O0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0  0QO0QO0QO0QO0QO0QO0    O0QO          QO0  0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO Q 0QO0QO0QO0QO0QO0QO   0QO             QO0 O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0Q  QO0QO0QO0QO0QO0QO0  0QO0              0QO QO0 O0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0 O0QO0QO0QO0QO0QO0QO QO0Q               O0Q 0QO QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0QO                QO0QO0Q 0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0QO0                 0QO0QO0 O0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0QO0QO                 O QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0                 0Q 0QO0Q 0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0QO               0QO  O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0QO0                     QO0Q 0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0Q                      0QO QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0                        Q 0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0Q                          QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0           0Q            O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0Q        QO Q            O QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0        0Q           QO Q  QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO        O0QO              O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0Q            O0        0Q  QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO               0Q          0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0Q                            0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0                   O Q     QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO                           0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0Q                           O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0                          0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO                         QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0Q               O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0               QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO               0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0Q            O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0             O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO             QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO            0QO0Q  QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0Q       0QO0QO0Q            O0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0         QO0QO0                 0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0Q            O0QO0QO                 O0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0Q           QO0QO0QO0QO0               QO0Q 0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0                 0QO0QO0QO0               QO QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO                       O0QO0QO            0Q 0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0Q                             QO0QO0QO      0Q 0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0                                 QO0QO0Q   O0 O0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO                                       0QO  O QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO                                        Q  QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0Q                                        0Q 0 O0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0                                        O0 O0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0                                        O QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0QO0                                      0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0Q   O0QO                             O0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0QO0    O0QO0Q        QO0QO              O0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0QO0QO0   QO0QO0QO0QO0QO0QO0  0            QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0  0QO0QO0QO0QO0QO0QO Q            O0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO   0QO0QO0QO0QO0QO0QO            0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO  O0QO0QO0QO0QO0QO0            QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q  QO0QO0QO0QO0QO0            QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0  0QO0QO0QO0QO0Q            O0QO0QO0QO0QO0Q 0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO  O0QO0QO0QO0QO             QO0QO0QO0QO0QO0 O0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO QO0QO0QO0QO0             O0QO0QO0QO0QO0QO QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q 0QO0QO0QO0Q             0QO0QO0QO0QO0QO0Q 0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO  O0QO0QO0QO0            QO0QO0QO0QO0QO0QO0 O0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q  QO0QO0QO              O0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0  0QO0QO0              0QO0QO0QO0QO0QO0QO0Q  QO0Q
O0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q  QO0QO0               QO0QO0QO0QO0QO0QO0QO0Q  QO0
QO0QO0QO0QO0QO QO0QO0QO0QO0QO   0QO0               QO0QO0QO0QO0QO0QO0QO0 O0Q 0QO
0QO0QO0QO0QO0Q 0QO      0QO0   QO0QO              O0QO0QO0QO0QO0QO0QO0QO0 O0 O0Q
O0QO0QO0QO0QO  O          Q   O0QO0Q    0       O0QO0QO0QO0QO0QO0QO0QO0QO0 O0QO0
QO0QO0QO0QO0Q       0QO0     0QO0QO0           0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0      QO0QO0   QO0QO0QO0  0       O0QO0QO0QO0QO0QO0QO0QO0QO0QO QO0Q
O0QO0QO0QO0QO     O0QO0Q   O0QO0QO0QO0Q        QO0QO0QO0QO0QO0QO0QO0QO0QO Q 0QO0
QO0QO0QO0QO0Q    0QO0Q   O  O0QO0QO0QO          QO0QO0QO0QO0QO0QO0QO0QO0Q  QO0QO
0QO0QO0QO0QO0   QO0Q    0Q  QO0QO0Q              QO0QO0QO0QO0QO0QO0QO0QO0 O QO0Q
O0QO0QO0QO0QO  O0Q    0QO0  0QO0QO                QO0QO0QO0QO0QO0QO0QO0QO0Q 0QO0
QO0QO0QO0QO0Q  QO   0QO0QO  O0QO0Q                  O0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0 O0   QO0QO0Q 0QO0QO         0Q             0QO0QO0QO0QO0QO0 O QO0Q
O0QO0QO0QO0QO0Q   O0QO0QO  O0QO           O0Q         O0QO0QO0QO0QO0QO0QO QO0QO0
QO0QO0QO0QO0QO0  0QO0QO0Q  QO0Q 0         QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q   O0QO
0QO0QO0QO0QO0Q  QO0QO0QO  O0QO            0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0 O0QO0Q
O0QO0QO0QO0QO0  0QO0QO0  0QO0QO            0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0  0QO0   QO0QO0QO            0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO       QO0QO0QO0QO0           0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0   QO0QO0QO0QO0QO0Q           QO0QO0QO0QO0QO0QO0QO0QO0QO Q 0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0            QO  O0QO0QO0QO0QO0QO0Q  QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0               QO0QO0QO0QO0QO0QO0   QO0Q
O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q         O0QO0QO0QO0QO0QO0QO0QO QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0     0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0Q
O0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0
QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO0QO
```

Setting width to 50 pixels and character set to `"JOKER"`

```
(venv) ...imascii>python main.py "/images/card.jpg" -wt 50 -c JOKER -ht 50

original image: width=188, height=269
resized image: width=50, height=50
JOKERJOKERJOKERJOKERJOKERJOKERJOKERJOKERJOKERJOKER
JOKERJOKERJOKERJOKERJOKERJOKERJOKERJOKERJOKERJOKER
JOKERJOKERJOKERJOKERJOKER   ERJOKERJOKERJOKERJOKER
JOKERJOKERJOKERJOKERJOKER  KERJOKERJOKERJOKERJOKER
JOKERJOKERJOKERJOKERJOKE   KERJOKERJOKERJOKERJOKER
JOKERJOKERJOKERJO    O  R      OKERJOKERJOKERJOKER
JOKERJOKERJOKE                  KERJOKERJOKERJOKER
JOKERJOKERJ    JOKER   E      J  ERJOKERJOKERJOKER
JOKERJOKER   ERJOKERJ            ERJOKERJOKERJOKER
JOKERJOKE  OKERJOKER      O      ERJOKERJOKERJOKER
JOK RJOKERJOKERJOK    K         KERJOKERJOKERJOKER
JOKERJOKERJOKERJO   JOKE   K    KERJOKERJOKERJOKER
JOKERJOKERJOKERJ   RJ      KER OKERJOKERJOKERJOKER
JOK RJOKERJOKERJ KE         ER OKERJOKERJOKERJOKER
JOKERJOKERJOKERJOK          ERJOKERJOKERJOKERJOKER
JOKERJOKERJOKERJO           ERJOKERJOKERJOKERJOKER
JOKERJOKERJOKERJ             RJOKERJOKERJOKERJOKER
JOKERJOKERJOKER                OKERJOKERJOKERJOKER
JOKERJOKERJOKER                OKERJOKERJOKERJOKER
JOKERJOKERJOKE                 OKERJOKERJOKERJOKER
JOKERJOKERJOKE                 OKERJOKERJOKERJOKER
JOKERJOKERJOKE                 OKERJOKERJOKERJOKER
JOKERJOKERJOKE                JOKERJOKERJOKERJOKER
JOKERJOKERJOKE         ERJOKERJOKERJOKERJOKERJOKER
JOKERJOKERJOKE         ERJOKERJOKERJOKERJOKERJOKER
JOKERJOKERJOKE        KERJOKERJOKERJOKERJOKERJOKER
JOKERJOKERJOKE      JOKE        KERJOKERJOKERJOKER
JOKERJOKERJOKE       OKERJ            ERJOKERJOKER
JOKERJOKERJOKE             KERJO         OKERJOKER
JOKERJOKERJOKER                     OK   OKERJOKER
JOKERJOKERJOKER                         J KERJOKER
JOKERJOKERJOKER                         J KERJOKER
JOKERJOKERJOKERJO                       JOKERJOKER
JOKERJOKERJOKERJOK  JOKERJOKERJO        JOKERJOKER
JOKERJOKERJOKERJOKE  OKERJOKERJ        RJOKERJOKER
JOKERJOKERJOKERJOKE  OKERJOKE        KERJOKERJOKER
JOKERJOKERJOKERJOKER OKERJOK        OKERJOKERJOKER
JOKERJOKERJOKERJOKER OKERJO        JOKERJOKERJOKER
JOKERJOKERJOKERJOKE JOKER        ERJOKERJOKERJOKER
JOKERJOKERJOK RJOK  JOK        OKERJOKERJOKERJOKER
JOKERJOK     ER   ERJOK       JOKERJOKERJOKERJOKER
JOKERJOK   OKER  KERJOKE      JOKERJOKERJOKERJ KER
JOKERJOK  JO  RJ KERJO         OKERJOKERJOKERJOKER
JOKERJOK R  KERJ KERJ      K      RJOKERJOKERJOKER
JOKERJOKE  OKER  KE       OKERJOKERJOKERJOKERJ KER
JOKERJOKE JOKE  OKE        KERJOKERJOKERJOKERJOKER
JOKERJOKER   ERJOKERJO       RJOKERJOKERJOKERJOKER
JOKERJOKERJOKERJOKERJOKER         RJOKERJOKERJ KER
JOKERJOKERJOKERJOKERJOKERJOKE  OKERJOKERJOKERJOKER
JOKERJOKERJOKERJOKERJOKERJOKERJOKERJOKERJOKERJOKER
```
