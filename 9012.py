import sys
T = int(sys.stdin.readline().rstrip())

for i in range(T) :
    c = list(sys.stdin.readline().rstrip())
    f = False
    stack = []
    for j in c :
        if j == '(' :
            stack.append(j)
        elif j == ')':
          if (len(stack) == 0) : 
              f = True
          else :
              stack.pop()

    if f == False and len(stack) == 0 :
        print('YES')
    else :
        print('NO')