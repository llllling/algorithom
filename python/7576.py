import sys
from collections import deque
m, n = map(int, sys.stdin.readline().rstrip().split())
box = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# queue로 했을 때 시간초과 나서 deque 로 변경
# 연산의 복잡도에 있어 deque이 더 빠르게 동작하도록 설계되어 있다고 한다

visited = deque()
x = [0, -1, 1, 0]
y = [-1, 0, 0, 1]

def BFS() :
    while len(visited) > 0 :
        tmp = visited.popleft()
        a = tmp[0]
        b = tmp[1]

        for i in range(4) :
            ax = a + x[i]
            by = b + y[i]
            if ax < 0 or by < 0 or ax >= n or by >= m :
                continue
            if box[ax][by] == 0 :
                box[ax][by] = box[a][b] + 1
                visited.append([ax, by])


for i in range(n) :
    for j in range(m) :
        if box[i][j] == 1 :
            visited.append([i,j]) 
BFS()
#처음 소스코드 짤때는 i, j 하나씩 방문하면서 1일경우 bfs를 실행했었다. 
# 그래서 안댔움. 만약 0,0 이 1 이고 맨마지막 행,열이 1이면 동시에 스타트해서 방문한 느낌이여야하는데 
# 0,0의 1부터 시작해서 해버리니까 날짜 카운트가 이상했음 

check = False
maxValue = box[0][0]
for i in range(n) :
    for j in range(m) :
        if box[i][j] == 0 : 
            check = True
            break
        maxValue = max(box[i][j], maxValue)

if check == True: 
    print(-1)
elif maxValue == -1 :
    print(0)
else :
    print(maxValue - 1)