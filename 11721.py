import sys
t = list(sys.stdin.readline().rstrip())
str = ''
for i in range(len(t)) :
  str += t[i]
  if ((i + 1) % 10 == 0 or (i + 1) == len(t)) :
    print(str)
    str = ''
  
  