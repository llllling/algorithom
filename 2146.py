import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

m = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]


vis = [[False] * N for _ in range(N)]
x = [-1, 0, 1, 0]
y = [0, 1, 0, -1]
ans = sys.maxsize

def dfs(i, j,r) : #������ �󺧸� �ٸ��� ��� ���湮 dfs�� 
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


def bfs(r) : #������ ��� ã�� ��� bfs�� 
    global ans
    dist = [[-1] * N for _ in range(N)]
    visit2 = deque()

    #�� ���� ���� deque�� �־ �ִܰŸ� ����
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
            if  m[ax][by] > 0 and m[ax][by] != r : #����̰� �ٸ� ��� �� ���
                ans = min(ans, dist[a][b]) #�ٸ� ������ �������� �� �ִܰŸ� ���� ���ϱ����� ��
                return

            if m[ax][by] == 0 and dist[ax][by] == -1 : #�ٴ��̰� ���� �湮���ߴٸ� 
                 #�ִܰŸ����� + 1, �ش������� ���� �湮���ѰŴϱ� ���� a,b���� +1 ������ ���� �ִܰŸ��̴�.
                dist[ax][by] = dist[a][b] + 1 
                visit2.append([ax, by])
            


# ���� ������ŭ 
for i in range(2, r) :
  bfs(i) 

print(ans)