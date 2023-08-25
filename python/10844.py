import sys
N = int(sys.stdin.readline().rstrip())
dp = []
for i in range(N) :
    if (i == 0) :
        dp.append([0,1,1,1,1,1,1,1,1,1])
    else : 
        x = []
        for j in range(10) :
            if (j == 0) :
                x.append(dp[i-1][1])
            elif (j == 9) :
                x.append(dp[i-1][8])
            else :
                x.append(dp[i-1][j-1] + dp[i-1][j+1])
        dp.append(x)

print(sum(dp[N-1]) % 1000000000)