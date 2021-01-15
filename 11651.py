import sys
N = int(sys.stdin.readline().rstrip())
A = []

for i in range(N) :
  A.append(list(reversed(list(map(int,sys.stdin.readline().rstrip().split())))))
A.sort()

for i in range(N) :
  print(A[i][1], A[i][0])