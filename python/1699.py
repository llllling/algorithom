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
        ## <dp[i - j * j] + 1�� ���� �ؼ�>
        ## 1. dp[i - (i���� ���� ������)] ��, i - ������ = ������ ex) 5 = 2����(4) + 1 �̴�. ���⼭ 1�� �ǹ�
        ## 2. �÷��� 1 ���ִ� �� ������ 1�� �ǹ� 

print(dp[N])    
        