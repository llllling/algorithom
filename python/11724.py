import sys
import queue
N, M = map(int, sys.stdin.readline().rstrip().split())
g = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M) :
    u, v = map(int, sys.stdin.readline().rstrip().split())
    g[u][v] = 1
    g[v][u] = 1

visited = [0 for _ in range(N + 1)] # 첨에 in, not in 할때는 빈배열로 초기화했었음 
def DFS(graph, start) :
    need_visit = queue.LifoQueue()
    need_visit.put(start)

    while need_visit.qsize() > 0 :
        v = need_visit.get()
        #  if v not in visited로 했을 때 시간초과 떳음., 
        # in, not in 시간복잡도 O(N), 아래와 같이 바로 인덱스로 접근 O(1) 
        if visited[v] == 0 :
            visited[v] = 1
            for i in range(1, N + 1) :
                if graph[v][i] == 1 :
                    need_visit.put(i)


answer = 0
for i in range(1, N + 1):
    # 첨에 위에 처럼 not in 으로 체크했었음
    if visited[i] == 0:
        DFS(g, i)
        answer += 1

print(answer)