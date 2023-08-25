import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T) :
    n = int(sys.stdin.readline().rstrip())
    student = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    visit = [0 for _ in range(n + 1)] #전체 방문 체크 
    result = []
    for j in range(1, n + 1) :
        if visit[j] == 0 :
            loop = [j] #순환그래프인 지 체크
            visit[j] = 1
            t = student[j]
            while visit[t] == 0 :
                loop.append(t)
                visit[t] = 1
                t = student[t]
            if t in loop :
                result += loop[loop.index(t) :]

    print(n - len(result))



