# references:
#   python open zip file: https://docs.python.org/2/library/gzip.html
#   python byte convert to int: https://docs.python.org/3/library/stdtypes.html#int.from_bytes
#   

# use python open a file
import gzip
f = gzip.open('data/t10k-labels-idx1-ubyte.gz','rb')
# read firt 4 bytes
magic = f.read(4)
print("magic number is: "+str(int.from_bytes(magic,'big')))
# read next 4 bytes
nolab = f.read(4)
nolab = int.from_bytes(nolab,'big')
print("number of labels is:",nolab)

#labels = []
#for i in range(nolab):
#    labels.append(f.read(1))
labels = [f.read(1) for i in range(nolab)]


 