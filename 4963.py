import sys
import queue

def BFS(s) : 
    need_v = queue.Queue()
    need_v.put(s)
    x = [-1, 0, 1]
    y = [-1, 0, 1]
    while need_v.qsize() > 0 :
        tmp = need_v.get()
        a = tmp[0]
        b = tmp[1]
        if m[a][b] == 1 :
            m[a][b] = 0
            for xx in x :
                for yy in y :
                    ax = a + xx 
                    by = b + yy 
                    if ax < 0 or by < 0 or ax >= h or by >= w :
                        continue
                    if m[ax][by] == 1 :
                        need_v.put([ax, by])
            
w, h = map(int, sys.stdin.readline().rstrip().split())
while w > 0 and h > 0 :
    m = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
    result = 0 
    for i in range(h) :
        for j in range(w) :
            if m[i][j] == 1 :
                result += 1
                BFS([i,j])
    print(result)
    w, h = map(int, sys.stdin.readline().rstrip().split())
