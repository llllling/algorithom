import sys
N = int(sys.stdin.readline().rstrip())
dp = []
for i in range(N) :
    if i == 0 :
        dp.append([0, 1])
    else :
        x = []
        x.append(dp[i - 1][0] + dp[i - 1][1])
        x.append(dp[i - 1][0])
        dp.append(x)

print(sum(dp[N-1]))