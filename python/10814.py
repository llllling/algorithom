import sys
N = int(sys.stdin.readline().rstrip())
A = []
for i in range(N) :
  t = sys.stdin.readline().rstrip().split()
  A.append([int(t[0]), i, t[1]])

A.sort()

for i in range(N) :
  print(A[i][0], A[i][2])

