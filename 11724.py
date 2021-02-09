import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
g = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M) :
    u, v = map(int, sys.stdin.readline().rstrip().split())
    g[u][v] = 1
    g[v][u] = 1
