import sys
import queue
N = int(sys.stdin.readline().rstrip())
array = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]

def BFS(s) :
    x = [-1, 0, 1, 0]
    y = [0, -1, 0, 1]

    need_v = queue.LifoQueue()
    need_v.put(s)
    num = 0

    while need_v.qsize() > 0 :
        t = need_v.get()
        nx = t[0]
        ny = t[1]
        if array[nx][ny] == 1 :
            array[nx][ny] = 0 # 방문했던 곳은 0으로 치환
            num += 1
            for i in range(4) :
                a = nx + x[i]
                b = ny + y[i]

                if a < 0 or b < 0 or a >= N or b >= N :
                    continue
                if array[a][b] == 1 : need_v.put([a, b])        
    return num

numArray = []

for j in range(N) :
    for k in range(N) :
        if array[j][k] == 1 :
            numArray.append(BFS([j,k]))

print(len(numArray))
numArray.sort()
for x in numArray :
    print(x)
