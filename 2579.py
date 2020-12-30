import sys
n = int(sys.stdin.readline().rstrip())
A = []
for i in range(n) :
  A.append(int(sys.stdin.readline().rstrip()))

dp = [A[n - 1]]
for i in range(n - 2, -1, -1) :
  dp.append()
