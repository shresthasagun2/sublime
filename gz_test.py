import sys
import gzip

#places argument provided by the user in filename
#sys.argv[0] is the python file, in our case 1_cat.py is the value for sys.argv[0]

filename = sys.argv[1]

f = gzip.open(filename, 'rw')
file_content = f.read()
for rows in file_content:
    print rows
f.close()