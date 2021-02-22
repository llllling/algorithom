import sys
import queue

N, M = map(int, sys.stdin.readline().rstrip().split())
g = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M) :
    u, v = map(int, sys.stdin.readline().rstrip().split())
    g[u][v] = 1
    g[v][u] = 1

visited = []

def DFS(graph, start, result) :
    need_visit = queue.LifoQueue()
    need_visit.put(start)
    s = 0
    check = False
    while need_visit.qsize() > 0 :
        v = need_visit.get()

        if v not in visited :
            check = True
            visited.append(v)
            for i in range(1, N + 1) :
                if graph[v][i] == 1 :
                    need_visit.put(i)
                elif i not in visited:
                    s = i
    if check : 
        result += 1
        check = False
    if s != 0 : 
        DFS(graph, s, result)

    return result    


print(DFS(g, 1, 0))