import sys
N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().rstrip().split()))

P.sort()

A = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    A[i] += A[i - 1] + P[i - 1]

result = sum(A)
print(result)
