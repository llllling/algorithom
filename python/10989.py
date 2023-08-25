import sys
N = int(sys.stdin.readline().rstrip())
A = [0 for _ in range(10001)]
m = 0
for i in range(N) :
  t = int(sys.stdin.readline().rstrip())
  A[t] += 1
  
  if t > m :
    m = t
  

for i in range(1, m + 1) :
  for j in range(A[i]) :
    print(i)