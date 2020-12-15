import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rstrip().split()))
dp = [A[0]]
for i in range(1, N) :
    dp.append(A[i])
    for j in range(i - 1, -1, -1) :
       if (A[i] > A[j] and dp[i] < A[i] + dp[j]) :
           dp[i] = A[i] + dp[j]
print(max(dp))