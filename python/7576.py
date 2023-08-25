import sys
from collections import deque
m, n = map(int, sys.stdin.readline().rstrip().split())
box = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# queue�� ���� �� �ð��ʰ� ���� deque �� ����
# ������ ���⵵�� �־� deque�� �� ������ �����ϵ��� ����Ǿ� �ִٰ� �Ѵ�

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
#ó�� �ҽ��ڵ� ©���� i, j �ϳ��� �湮�ϸ鼭 1�ϰ�� bfs�� �����߾���. 
# �׷��� �ȴ��. ���� 0,0 �� 1 �̰� �Ǹ����� ��,���� 1�̸� ���ÿ� ��ŸƮ�ؼ� �湮�� �����̿����ϴµ� 
# 0,0�� 1���� �����ؼ� �ع����ϱ� ��¥ ī��Ʈ�� �̻����� 

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