import sys
import queue

N, M = map(int, sys.stdin.readline().rstrip().split())
g = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M) :
    u, v = map(int, sys.stdin.readline().rstrip().split())
    g[u][v] = 1
    g[v][u] = 1

def DFS(graph, start) :
    visited = []
    need_visit = queue.LifoQueue()

    need_visit.put(start)

    while len(need_visit) > 0 :
        v = need_visit.get()

        if v not in visited :
            visited.append(v)
            for i in graph[v] :
                need_visit.put(graph[v])