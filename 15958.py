import sys
# N = int(sys.stdin.readline().rstrip())
# i = 0
# arr = []
# minY = sys.maxsize
# while i < N:
#     x, y = map(int, sys.stdin.readline().rstrip().split())

#     if(i > 0 and i % 2 == 0) :
#       minY = min(minY, y)
#     arr.append({'x' : x, 'y': y})
#     i += 1

file =  open("input.txt", 'r')
N = int(file.readline())
i = 0
arr = []
minY = sys.maxsize
while i < N :
  x, y = map(int, file.readline().rstrip().split())

  if(i > 0 and i % 2 == 0) :
    minY = min(minY, y)
  arr.append({'x' : x, 'y': y})
  i += 1
file.close()

def right(i, x, y) :
    area = x * y
    j = i + 2
    while j < N:
      y = min(y, arr[j]['y'])
      if (y == minY) : 
        area += minY * (arr[N - 1]['x'] - x)
        break
      x = arr[j]['x'] - x
      area += x * y
      x = arr[j]['x']
      j += 2
    return area

def left(i, x, y) :
    area = x * y
    j = i - 2
    while j > 0:
      y = min(y, arr[j]['y'])
      if (y == minY) : 
        area += minY * (arr[N - 1]['x'] - x)
        break
      x = arr[j]['x'] - x
      area += x * y
      x = arr[j]['x']
      j -= 2
    return area

i = 2
result = minY * arr[N - 1]['x']
while i < N :
  if (arr[i]['y'] != minY) :
      y = arr[i]['y']
      x = arr[i]['x']
      result = max(result, right(i, x, y))
      result = max(result, left(i, x, y)) 
  i += 2

print(result)
