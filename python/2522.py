import sys
N = int(sys.stdin.readline().rstrip())
y = ""
for i in range(1, 2*N) :
    if i <= N :
        y = str(" " * (N - i)) + str("*" * i)
    else :
        y = str(" " * (i - N)) + str("*" * ((2*N)-i))
    print(y)
    i += 1
