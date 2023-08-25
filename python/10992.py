import sys
N = int(sys.stdin.readline().rstrip())
x = ""
for i in range(1, N+1) :
  x = ""
  for j in range(1, N+i) :
    if (j == N+i-1 or i > 1 and j == (N-i+1) or i == N) : 
      x += "*"
    else :
      x += " "
    j += 1
  print(x)
  i += 1