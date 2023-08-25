import sys
N = int(sys.stdin.readline().rstrip())

for x in range(1, 10) :
  print(N,"*", x,"=",x * N)