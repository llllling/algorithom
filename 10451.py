import sys
import queue
T = int(sys.stdin.readline().rstrip())

for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    v = [0 for _ in range(N + 1)]
    array = [0] + list(map(int,sys.stdin.readline().rstrip().split()))
    v[1] = 0
    result = 0
    for j in range(1, N + 1):
        t = array[j]
        if v[t] == 0 : result += 1
        while v[t] == 0:
            v[t] = 1
            t = array[t]
    print(result)
  