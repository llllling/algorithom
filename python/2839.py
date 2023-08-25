import sys
N = int(sys.stdin.readline().rstrip())

a = [0 for _ in range(N)]
a[0] = 1
a[1] = -1
a[2] = 1

for i in range(3, N - 2):
    a[i] = -1
    if i >= 5:
        if a[i - 5] == -1:
            a[i] = -1
        else:
            a[i] = a[i - 5] + 1

    if a[i] == -1 and i >= 3:
        if a[i - 3] == -1:
            a[i] = -1
        else:
            a[i] = a[i-3] + 1

print(a[N - 3])
