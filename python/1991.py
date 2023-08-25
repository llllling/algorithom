import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
tree = {}
for i in range(N) :
    a, b, c = sys.stdin.readline().rstrip().split()
    tree[a] = {
        'root' : a,
        'left' : b,
        'right' : c
    }

#임의의 경로를 찾는거다! 중위순회, 후위순회, 전위순회니까 임의의 경로임 > bfs
def bfs(type) : 
    q = deque()
    result = []

    for x in type : 
        if x == 'root' :
             

        
        




for i in [['root', 'left', 'right'], ['left', 'root', 'right'], ['left','right', 'root']] :
    print(bfs(i))


