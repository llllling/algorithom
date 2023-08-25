import sys

for x in sys.stdin :
  A, B = map(int, x.rstrip().split())
  if A == 0 & B == 0 : break
  print(A + B)