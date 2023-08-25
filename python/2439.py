import sys
N = int(sys.stdin.readline().rstrip())
i = 0
for i in range(N, 0, -1) :
    j = 1
    x =""
    for j in range(1, N + 1) :
        if (j >= i) :
            x += "*"
        else :
            x += " "
        j += 1
    print(x)
    i -= 1