import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

m = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]


vis = [[False] * N for _ in range(N)]
x = [-1, 0, 1, 0]
y = [0, 1, 0, -1]
ans = sys.maxsize

def dfs(i, j,r) : #섬마다 라벨링 다르게 모든 노드방문 dfs로 
    visit1 = deque()
    visit1.append([i, j])
    vis[i][j] = True
    m[i][j] = r

    while len(visit1) > 0 :
        a, b = visit1.pop()

        for i in range(4) :
            ax = a + x[i]
            by = b + y[i]
            if ax < 0 or by < 0 or ax >= N or by >= N :
                continue
            if m[ax][by] == 1 and not vis[ax][by]:
                m[ax][by] = r
                vis[ax][by] = True
                visit1.append([ax, by])
r = 2
for i in range(N) :
    for j in range(N) :
        if m[i][j] == 1 :
            dfs(i,j,r) 
            r += 1


def bfs(r) : #임의의 경로 찾을 경우 bfs로 
    global ans
    dist = [[-1] * N for _ in range(N)]
    visit2 = deque()

    #한 개의 섬씩 deque에 넣어서 최단거리 측정
    for i in range(N) :
        for j in range(N) :
            if m[i][j] == r :
                dist[i][j] = 0
                visit2.append([i,j])

    while len(visit2) > 0 :
        a, b = visit2.popleft()
        for i in range(4) :
            ax = a + x[i]
            by = b + y[i]
            if ax < 0 or by < 0 or ax >= N or by >= N :
                continue
            if  m[ax][by] > 0 and m[ax][by] != r : #대륙이고 다른 대륙 일 경우
                ans = min(ans, dist[a][b]) #다른 섬에서 시작했을 때 최단거리 값과 비교하기위한 것
                return

            if m[ax][by] == 0 and dist[ax][by] == -1 : #바다이고 아직 방문안했다면 
                 #최단거리에서 + 1, 해당지역을 아직 방문안한거니까 현재 a,b에서 +1 증가한 값이 최단거리이다.
                dist[ax][by] = dist[a][b] + 1 
                visit2.append([ax, by])
            


# 섬의 갯수만큼 
for i in range(2, r) :
  bfs(i) 

print(ans)