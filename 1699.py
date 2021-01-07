import sys
N = int(sys.stdin.readline().rstrip())
dp = [0]

for i in range(1, N + 1) :
    dp.append(i)

    for j in range(2, i) :
        if j * j > i :
            break
        
        if dp[i] > dp[i - j * j] + 1 :
            dp[i] = dp[i - j * j] + 1
        ## <dp[i - j * j] + 1에 대한 해설>
        ## 1. dp[i - (i보다 작은 제곱수)] 즉, i - 제곱수 = 나머지 ex) 5 = 2제곱(4) + 1 이다. 여기서 1을 의미
        ## 2. 플러스 1 해주는 건 제곱수 1개 의미 

print(dp[N])    
        