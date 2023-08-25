import sys
import queue

A, P = map(int, sys.stdin.readline().rstrip().split())
array = queue.Queue()
array.put(A)
v = []
t = 0
while array.qsize() > 0 :
    t = array.get()
    if t not in v :
        v.append(t)
        res = [int(x) ** P for x in str(t)] 
        array.put(sum(res))

print(v.index(t))
