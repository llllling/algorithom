import sys
T = int(sys.stdin.readline().rstrip())

dp = [0, 1, 2, 4]
for i in range(T) :
    n = int(sys.stdin.readline().rstrip())
    if n > len(dp) - 1 :
        for j in range(len(dp), n + 1) :
            dp.append(dp[j - 1] + dp[j - 2] + dp[j - 3])
    print(dp[n])
