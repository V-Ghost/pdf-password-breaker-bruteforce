from joblib.numpy_pickle_utils import xrange

myfile = open('6_digit_code.txt', 'w')
import itertools


for i in itertools.product(xrange(10), repeat=6):
  myfile.write("%s\n" % ''.join(map(str, i)))
myfile.close()