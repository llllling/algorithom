import sys
n = int(sys.stdin.readline().rstrip())
A = []
for i in range(n) :
  A.append(int(sys.stdin.readline().rstrip()))

dp = [A[0]]

for i in range(1, n) :
  if i == 1 : 
    dp.append(A[0] + A[1])
  elif i == 2 :
    dp.append(max(A[0] + A[2], A[1] + A[2]))
  else : 
    dp.append(max(dp[i - 2] + A[i], dp[i - 3] + A[i-1] + A[i]))

print(dp[n-1])