import sys
N = int(sys.stdin.readline().rstrip())
A = {}

for i in range(N) :
    t = int(sys.stdin.readline().rstrip())
    if t in A :
        A[t] += 1
    else : 
        A[t] = 1     

result = sorted(A.items(), key=lambda x: (-x[1], x[0]))

print(result[0][0])