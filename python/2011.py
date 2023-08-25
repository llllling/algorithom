import sys
A = list(map(int,sys.stdin.readline().rstrip()))
dp = [0 for _ in range(len(A) + 1)]

if A[0] == 0 :
  print(0)
else :
  dp[0] = 1
  dp[1] = 1
  
  for i in range(2, len(A) + 1) :
    if A[i - 1] > 0 and A[i - 1] < 10 :
      dp[i] = dp[i - 1]

    if A[i - 2] * 10 + A[i - 1] > 9 and A[i - 2] * 10 + A[i - 1] < 27 :
      dp[i] += dp[i - 2]

  print(dp[len(A)] % 1000000)