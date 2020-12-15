import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rstrip().split()))
dpA = [1]
dpB = [1]
dp = []
for i in range(1, N) :
    dpA.append(1)

    for j in range(i - 1, -1, -1) :
        if A[i] > A[j] and dpA[i] <= dpA[j]:
            dpA[i] = dpA[j] + 1

    dpB.append(1)
     for j in range(N - 1, i, -1) :
        if A[i] > A[x] and dpB[i] <= dpB[x]:
            dpB[i] = dpB[x] + 1
            
print(max(dp))