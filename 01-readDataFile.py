# references:
#   python open zip file: https://docs.python.org/2/library/gzip.html
#   python byte convert to int: https://docs.python.org/3/library/stdtypes.html#int.from_bytes
#   

# //function to read labels from .gz file 
def read_lables(filename):
    # //use python open a file
    import gzip
    with gzip.open(filename,'rb') as f:
        # //read firt 4 bytes
        magic = f.read(4)
        print("magic number is: "+str(int.from_bytes(magic,'big')))
        # //read next 4 bytes
        nolab = f.read(4)
        nolab = int.from_bytes(nolab,'big')
        print("number of labels is:",nolab)
        # //save labels to a list
        #labels = []
        #for i in range(nolab):
        #    labels.append(f.read(1))
        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label,'big') for label in labels]
        #print(labels)
    return labels

test_labels = read_lables('data/t10k-labels-idx1-ubyte.gz')
train_labels = read_lables('data/train-labels-idx1-ubyte.gz')

# //function to read images from .gz file 
def read_images(filename):
    # //use python open a file
    import gzip
    with gzip.open(filename,'rb') as f:
        # //read firt 4 bytes
        magic = f.read(4)
        print("magic number is: "+str(int.from_bytes(magic,'big')))
        # //read next 4 bytes, the number of images
        noimg = f.read(4)
        noimg = int.from_bytes(noimg,'big')
        print("number of images is:",noimg)
         # //read next 4 bytes,the number of rows for each image
        norow = f.read(4)
        norow = int.from_bytes(norow,'big')
        print("number of rows is:",norow)
         # //read next 4 bytes,the number of columns for each image
        nocol = f.read(4)
        nocol = int.from_bytes(nocol,'big')
        print("number of columns is:",nocol)
        # //save images to a list
        images = [ ]
        for i in range(noimg):
            rows = [ ]
            for row in range(norow):
                columns = [ ]
                for col in range(nocol):
                    columns.append(int.from_bytes(f.read(1),'big'))
                rows.append(columns)
            images.append(rows)    
    #print(images)
    return images

test_images = read_images('data/t10k-images-idx3-ubyte.gz')
train_images = read_images('data/train-images-idx3-ubyte.gz')


 