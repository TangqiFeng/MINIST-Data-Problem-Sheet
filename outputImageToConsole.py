# references:
#   import another python file: https://stackoverflow.com/questions/9123517/how-do-you-import-a-file-in-python-with-spaces-in-the-name
#   numpy.array: https://docs.scipy.org/doc/numpy-1.13.0/user/basics.creation.html

# //import read_data_file.py   
import readDataFile
import numpy as np
# the third image in the training set
myimage = readDataFile.train_images[3]
maimage = np.array(myimage)
for row in myimage:
    for col in row:
        print('.' if col<128 else '/',end='')
    print()
# train_images[3] is 1
# readDataFile.train_labels[3] ==> 1