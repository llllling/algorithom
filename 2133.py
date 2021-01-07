import sys
N = int(sys.stdin.readline().rstrip())

dp=[0 for _ in range(N + 1)]

for i in range(2, N + 1, 2) :
    if i == 2 :
        dp[2] = 3
        continue

# 8 
# 1. dp[6] * dp[2](끝에 2를 붙이는 경우)
# 2. dp[4] * 2(끝에 4(새로만들어진 모양 2개)를 붙이는경우)
# 3. dp[2] * 2(끝에 6(새로만들어진 모양 2개)를 붙이는경우)

    dp[i] = dp[i - 2] * dp[2] + 2 
    for j in range(4, i, 2) :
        dp[i] += 2 * dp[i - j]
    
print(dp[N])


