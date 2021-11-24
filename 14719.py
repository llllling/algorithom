import sys

h, w = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
for i in range(1, w - 1):
    left = max(arr[:i])
    right = max(arr[i + 1:])

    line = min(left, right)
    warter = line - arr[i]

    result += warter if warter > 0 else 0

print(result)
