import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1]

for i in range(1, N) :
  dp.append(1)
  for j in range(i - 1, -1, -1) :
    if (A[i] > A[j] and dp[i] <= dp[j]) :
      dp[i] = dp[j] + 1

print(max(dp))


