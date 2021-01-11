import sys
[N, K] = list(map(int, sys.stdin.readline().rstrip().split()))
dp = []
for i in range(0, N + 1):
    dp.append([0 ,1])
    for j in range(2, K + 1) :
        if i == 0 : 
            dp[i].append(1)
            continue

        dp[i].append(dp[i][j - 1])

        for x in range(0, i) :
            dp[i][j] += dp[x][j - 1]
    
print(dp[N][K] % 1000000000)