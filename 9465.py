import sys 
T = int(sys.stdin.readline().rstrip())

for x in range(T) :
  n = int(sys.stdin.readline().rstrip())
  s = []
  s.append(list(map(int,sys.stdin.readline().rstrip().split())))
  s.append(list(map(int,sys.stdin.readline().rstrip().split())))

  result = []
  result.append([0])
  result.append([0])
  result[0].append(s[0][0])
  result[1].append(s[1][0])
  for i in range(2, n + 1) :
    result[0].append(s[0][i - 1] + max(result[1][i - 1], result[1][i - 2]))
    result[1].append(s[1][i - 1] + max(result[0][i - 1], result[0][i - 2])) 
  print(max(result[0][n], result[1][n]))
