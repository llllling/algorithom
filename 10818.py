import sys
N = int(sys.stdin.readline().rstrip())
x = list(map(int,sys.stdin.readline().rstrip().split()))
print(min(x),max(x))