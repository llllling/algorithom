import sys
n = int(sys.stdin.readline().rstrip())
wine = [0]
for i in range(n) : 
  wine.append(int(sys.stdin.readline().rstrip()))

if n == 1 : 
  print(wine[1])
else :  
  dp = [0, wine[1], wine[1] + wine[2]]
  for x in range(3, n + 1) :
    dp.append(max(dp[x - 1], wine[x] + dp[x - 2], wine[x] + wine[x - 1] + dp[x - 3]))
  print(dp[n])
