import sys

filename = sys.argv[1]

count=0
f = open(filename, 'rw')
print sum(1 for _ in f)