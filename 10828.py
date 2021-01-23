import sys
N = int(sys.stdin.readline().rstrip())
stack = []

command = {
    'push' : lambda x : stack.append(x),
    'pop'  : lambda x : stack.pop() if len(stack) > 0 else -1,
    'size' : lambda x : len(stack),
    'empty' : lambda x : 1 if len(stack) == 0 else 0,
    'top' : lambda x : stack[len(stack) - 1] if len(stack) > 0 else -1
}

for i in range(N) :
    c = sys.stdin.readline().rstrip()
    if (c.find('push') != -1) :
        (pushCommand, pushValue) = c.split()
        command[pushCommand](int(pushValue))
    else :
        print(command[c](1))
