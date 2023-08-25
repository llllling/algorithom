import sys
N = int(sys.stdin.readline().rstrip())
A = []

for i in range(N) :
    A.append(int(sys.stdin.readline().rstrip()))
A.sort()

for i in range(N) :
    print(A[i])