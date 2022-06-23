import sys
N,K = map(int, sys.stdin.readline().rstrip().split())
coin = [ int(sys.stdin.readline().rstrip()) for _ in range(N)]
result = 0
num = K
for i in range(N-1, -1, -1) :
  [a, b] = divmod(num, coin[i])

  result += a
  num = b

print(result)


  