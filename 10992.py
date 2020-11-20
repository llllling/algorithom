import sys
N = int(sys.stdin.readline().rstrip())
x = ""
for i in range(1, N+1) :
  for j in range(1, N+i-1) :
    if (j == N+i-1) : 
      x += "*"
    elif (i > 1 and j == N-i-1) : 
      x += "*"
    else :
      x += " "
    j += 1
  print(x)
  i += 1