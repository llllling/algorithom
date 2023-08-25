import sys

for x in sys.stdin :
   print(sum(map(int,x.rstrip().split())))