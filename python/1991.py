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

#������ ��θ� ã�°Ŵ�! ������ȸ, ������ȸ, ������ȸ�ϱ� ������ ����� > bfs
def bfs(type) : 
    q = deque()
    result = []

    for x in type : 
        if x == 'root' :
             

        
        




for i in [['root', 'left', 'right'], ['left', 'root', 'right'], ['left','right', 'root']] :
    print(bfs(i))


