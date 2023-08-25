import sys
N = int(sys.stdin.readline().rstrip())
A = []

for i in range(N) :
  A.append(list(map(int,sys.stdin.readline().rstrip().split())))
A.sort()

for i in range(N) :
  print(A[i][0], A[i][1])