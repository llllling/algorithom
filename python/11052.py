import sys
N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [P[0]]
for i in range(1, N) :
    dp.append(P[i])
    for j in range(i // 2 + 1) :
        dp[i] = max(dp[i], dp[j] + dp[i - j - 1])
print(dp[N-1])