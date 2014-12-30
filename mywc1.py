import sys
import gzip

filename = sys.argv[1]

f = gzip.open(filename, 'rw')
file_content = f.read()
for rows in file_content:
	print sum(1 for _ in file_content)