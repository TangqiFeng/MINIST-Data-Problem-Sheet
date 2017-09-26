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


 