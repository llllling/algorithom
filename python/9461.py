import sys
T = int(sys.stdin.readline().rstrip())

for i in range(T) :
    N = int(sys.stdin.readline().rstrip())
    dp = [0, 1, 1, 1, 2, 2]
    for j in range(6, N + 1) :
        dp.append(dp[j - 1] + dp[j - 5])
    print(dp[N])
