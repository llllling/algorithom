import sys
N = int(sys.stdin.readline().rstrip())
i = 0

for i in range(1, N + 1) :
    j = 0
    x = ""
    for j in range(i) :
         x += "*"
         j += 1
    print(x)
    i += 1
