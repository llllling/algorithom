import sys
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

temp = [0 for _ in range(n)]

for i in range(n):
    temp[i] = max(temp[i-1] + A[i], A[i])
        
print(max(temp))
