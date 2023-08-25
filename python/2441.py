import sys
N = int(sys.stdin.readline().rstrip())
for i in range(N, 0, -1) :
    print(str( " " * (N - i))+str( "*" * i))
    i -= 1
