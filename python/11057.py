import sys
N = int(sys.stdin.readline().rstrip())
dp = []
for i in range(N) :
    if (i == 0) :
        dp.append([1,1,1,1,1,1,1,1,1,1])
    else : 
        x = []
        for j in range(10) :
                x.append(sum(dp[i-1][j:10]))
        dp.append(x)

print(sum(dp[N-1]) % 10007)