import sys
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(n) :
    dp = [sum(x) for x in A]

print()
