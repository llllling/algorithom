import sys
import queue
N, M = map(int, sys.stdin.readline().rstrip().split())
g = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M) :
    u, v = map(int, sys.stdin.readline().rstrip().split())
    g[u][v] = 1
    g[v][u] = 1

visited = [0 for _ in range(N + 1)] # ÷�� in, not in �Ҷ��� ��迭�� �ʱ�ȭ�߾��� 
def DFS(graph, start) :
    need_visit = queue.LifoQueue()
    need_visit.put(start)

    while need_visit.qsize() > 0 :
        v = need_visit.get()
        #  if v not in visited�� ���� �� �ð��ʰ� ����., 
        # in, not in �ð����⵵ O(N), �Ʒ��� ���� �ٷ� �ε����� ���� O(1) 
        if visited[v] == 0 :
            visited[v] = 1
            for i in range(1, N + 1) :
                if graph[v][i] == 1 :
                    need_visit.put(i)


answer = 0
for i in range(1, N + 1):
    # ÷�� ���� ó�� not in ���� üũ�߾���
    if visited[i] == 0:
        DFS(g, i)
        answer += 1

print(answer)