import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rstrip().split()))

dpA = [1]
for i in range(1, N) :
    dpA.append(1)
    for j in range(i - 1, -1, -1) :
        if A[i] > A[j] and dpA[i] <= dpA[j] :
            dpA[i] = dpA[j] + 1
dpB = [1]
for i in range(N - 2, -1, -1) :
    dpB.append(1)
    for j in range(i + 1, N) :
        if A[i] > A[j] and dpB[N - i - 1] <= dpB[N - j - 1] :
            dpB[N - i - 1] = dpB[N - j - 1] + 1

dp = [x + y - 1 for (x, y) in zip(dpA, list(reversed(dpB)))]

print(max(dp))