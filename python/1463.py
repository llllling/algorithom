import sys
N = int(sys.stdin.readline().rstrip())

dp = [0, 0]
for i in range(2, N + 1) :
  x = N
  y = N
  z = N
  if (i % 2 == 0) :
    x = dp[i // 2] 
  if (i % 3 == 0) :
    y = dp[i // 3]
  z = dp[i - 1]
  dp.append(min([x, y, z]) + 1)

print(dp[N])
  