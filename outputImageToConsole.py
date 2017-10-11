# references:
#   import another python file: https://stackoverflow.com/questions/9123517/how-do-you-import-a-file-in-python-with-spaces-in-the-name
#   numpy.array: https://docs.scipy.org/doc/numpy-1.13.0/user/basics.creation.html

# //import read_data_file.py   
import readDataFile
import numpy as np
# read image in the training set
def readImage(no):
    myimage = readDataFile.train_images[no]
    myimage = np.array(myimage)
    return myimage
# print image to console
def printImage(myimage):
    for row in myimage:
        for col in row:
            print('.' if col<128 else '/',end='')
        print()

# let's say get the third image of the training set
printImage(readImage(3))
# train_images[3] is 1
# readDataFile.train_labels[3] ==> 1