import sys
import queue

N, M, V = map(int, sys.stdin.readline().rstrip().split())
g = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(M) :
    x,y = map(int, sys.stdin.readline().rstrip().split())

    g[x][y] = 1
    g[y][x] = 1


def BFS(graph, start) :
    visited = []
    need_visit = queue.Queue()
    need_visit.put(start)

    while need_visit.qsize() > 0 :
        c = need_visit.get()
        if c not in visited :
            visited.append(c)
            for i in range(N + 1) :
                if graph[c][i] == 1 : 
                    need_visit.put(i)
            
    return visited

def DFS(graph, start) :
    visited = []
    need_visit = queue.LifoQueue()
    need_visit.put(start)

    while need_visit.qsize() > 0 :
        c = need_visit.get()
        if c not in visited : 
            visited.append(c)
            for i in range(N, 0, -1) :
                if graph[c][i] == 1 : 
                    need_visit.put(i)
    return visited

a = DFS(g, V)
b = BFS(g, V)
for i in a :
    print(i, end=' ')
print()
for i in b :
    print(i, end=' ')