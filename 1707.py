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
    for k in range(1, V + 1):  # 연결 그래프가 아닐 수도 있으므로 각 정점 방문안한 곳 방문할 수 있도록,
        if vg[k] == 0:
            chk = BFS(g, k)
            # 연결 그래프가 아닐 경우 만약 그래프가 2개로 분할되어 있는 경우 1번그래프는 no인데 2번이 yes일 경우 이 조건 안넣어주면 yes 출력됨.
            if chk == False:
                break
    if chk:
        print("YES")
    else:
        print("NO")
