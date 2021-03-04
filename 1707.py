import sys
import queue

K = int(sys.stdin.readline().rstrip())


def BFS(g, start):
    nv = queue.Queue()
    nv.put(start)
    vg[start] = 1
    while nv.qsize() > 0:
        tmp = nv.get()
        for i in g[tmp]:
            if vg[i] == 0:
                vg[i] = -vg[tmp]
                nv.put(i)
            elif vg[i] == vg[tmp]:
                return False
    return True


for i in range(K):
    V, E = map(int, sys.stdin.readline().rstrip().split())
    g = [[] for _ in range(V + 1)]
    chk = True
    vg = [0 for _ in range(V + 1)]
    for j in range(E):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        g[a].append(b)
        g[b].append(a)
    for k in range(1, V + 1):
        if vg[k] == 0:
            chk = BFS(g, k)
            if chk == False:
                break
    if chk:
        print("YES")
    else:
        print("NO")
