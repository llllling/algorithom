import sys
N = int(sys.stdin.readline().rstrip())
x = ""
y = ""
for i in range(2*N, 1, -1) :
    if i <= N :
        x = str(" " * (i-2)) + str("*" * (N-i+2))
        y = str("*" * (N-i+1))
    else :
        x = str(" " * (2*N-i)) + str("*" * (i-N)) 
        y = str("*" * (i-N-1)) 
    print(str(x) + str(y))
    i -= 1
