import sys
N = int(sys.stdin.readline().rstrip())
for i in range(1, N + 1) :
    print(str( " " * (N - i)) + str( "*" * i) + str( "*"*(i - 1)))
    i += 1
