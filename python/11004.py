import sys
(N, K) = sys.stdin.readline().rstrip().split()
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()

print(A[int(K) - 1])