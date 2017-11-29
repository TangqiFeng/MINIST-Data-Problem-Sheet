# MINIST-Data-Problem-Sheet

> author: [Tangqi Feng](https://tangqifeng.github.io/)

These are solutions Solutions to the [Read Digits Image Files problem sheet](https://github.com/TangqiFeng/MINIST-Data-Problem-Sheet/wiki/MINIST-Data-Problem-Sheet)

> Module: Emerging Technologies / 4th Year  
> Lecturer: Dr [Ian McLoughlin](https://ianmcloughlin.github.io/)

These files work with the famous [MNIST](http://yann.lecun.com/exdb/mnist/) data set.
Please download the four data files from that website and place them (as gz files) in a subfolder called `data/`

## How this repository is organised
This repository include 3 files:
* readDataFile.py:<br/>
read labels & images from .gz file, and save it to array
* outputImageToConsole.py<br/>
read a image, and print it to console (import readDataFile.py)
* outputImageFile.py<br/>
output image files, both train_image and test_image (import outputImageToConsole.py)

## How to clone this repository
* Go to the [GitHub](https://www.github.com) [repository page](https://github.com/TangqiFeng/MINIST-Data-Problem-Sheet).
* Find the link to clone the repository.
### or
* just download the zip file

## How to run these scripts
go to the repository folder, open the command-line interpreter or terminal(mac), 

type ```$ python + title.py``` 

(title is the name of the file you wnat to execute)

## python3 is needed, [Install tutorial](https://anaconda.org/anaconda/python) 
**In addition, extensions: [PIL.Image](http://pillow.readthedocs.io/en/4.3.x/reference/Image.html), [gzip](https://docs.python.org/3/library/gzip.html), [numpy](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html) are need, make sure it is installed before run python files**
``` $ pip install pil / gzip / numpy ```
