import sys
n = int(sys.stdin.readline().rstrip())

dp = [0, 1, 2]

for i in range(3, n+1) :
  dp.append(dp[i - 1] + dp[i - 2])
  i += 1

print(dp[n]%10007)
