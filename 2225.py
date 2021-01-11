import sys
[N, K] = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [[1] for _ in range(N + 1)]

for i in range(1, N + 1):
  for j in range(2, K) :
    dp[i].append(dp[i][j - 1] + dp[i - j][j - 1])
    