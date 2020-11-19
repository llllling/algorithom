import sys
N = int(sys.stdin.readline().rstrip())
x = ""
y = ""
for i in range(1, 2*(N-1) + 2) :
    if i <= N :
        x = str("*" * i) + str(" " * (N - i))
        y = str(" " * (N - i)) + str("*" * i)
    else :
        x = str("*" * ((2*(N-1) +2) - i)) + str(" " * (i - N))
        y = str(" " * (i - N)) + str("*" * ((2*(N-1) +2) - i))
    print(str(x) + str(y))
    i += 1
