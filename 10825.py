import sys
N = int(sys.stdin.readline().rstrip())
A = []

for i in range(N) :
  t = sys.stdin.readline().rstrip().split()
  A.append([t[0], int(t[1]), int(t[2]), int(t[3])])

result = sorted(A, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(N) :
  print(result[i][0])