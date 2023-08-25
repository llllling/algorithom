import sys
T = int(sys.stdin.readline().rstrip())
i = 0

while i < T :
  A,B = map(int, sys.stdin.readline().rstrip().split())
  print(A+B)
  i += 1
