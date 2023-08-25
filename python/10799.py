import sys
C = list(sys.stdin.readline().rstrip())
laser = 0
result = 0
stack = []
for i in range(len(C)) :
    if (C[i] == '(') :
        if (C[i + 1] == ')') :
            if len(stack) == 0 : 
                continue
            laser += 1
        else :
            stack.append(-laser)
    else :
        if (C[i - 1] == '(') :
            continue
        result += stack.pop() + laser + 1

print(result)