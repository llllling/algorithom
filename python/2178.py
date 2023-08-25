import sys
from collections import deque

n,m = map(int, sys.stdin.readline().rstrip().split())
miro = [ list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)] 
visited = deque()
visited.append([0,0])

x = [-1, 0, 1, 0]
y = [0, 1, 0, -1]
while len(visited) > 0 :
    tmp = visited.popleft()
    a = tmp[0]
    b = tmp[1]

    for i in range(4) : 
        ax = a + x[i]
        by = b + y[i]

        if ax < 0 or by < 0 or ax >= n or by >= m :
            continue
        if miro[ax][by] == 1 :
            miro[ax][by] = miro[a][b] + 1 
            visited.append([ax, by])

print(miro[n - 1][m - 1])

