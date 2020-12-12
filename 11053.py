import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
result = 1
max = A[0]

for i in range(1, N) :
  if (max < A[i]) :
    max = A[i]
    result += 1
print(result)


