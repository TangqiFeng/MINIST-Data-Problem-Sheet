# references:
#   python open zip file: https://docs.python.org/2/library/gzip.html
#   python byte convert to int: https://docs.python.org/3/library/stdtypes.html#int.from_bytes
#   

# use python open a file
import gzip
f = gzip.open('data/t10k-labels-idx1-ubyte.gz','rb')
# read firt 4 bytes
magic = f.read(4)
print(int.from_bytes(magic,'big'))


 