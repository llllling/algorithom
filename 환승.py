import sys
import queue

INF = 10000000000
N = 4
transfer = [0,1,1,2,3]
n = len(transfer)
trainA = [[1,2,1],[1,3,3],[2,3,3]]
trainB = [[1,2,3],[2,3,2],[3,4,1]]
s = 1
e = 4
dist = [[{'A' : INF, 'B' : INF}  for _ in range(n) ] for _ in range(n)]
result = [[INF] * n for _ in range(n)]
#플로이드 와샬
def floyd_Warshall() :
  # 최단경로 담는 배열 초기화
  for i in trainA :
    dist[i[0]][i[1]]['A'] = i[2]
    dist[i[1]][i[0]]['A'] = i[2]
  for i in trainB :
    dist[i[0]][i[1]]['B'] = i[2]
    dist[i[1]][i[0]]['B'] = i[2]

  for k in range(1, n) :
    for i in dist[start] :
      for j in range(1, n) :
        oneA = dist[i][j]['A']
        oneB = dist[i][j]['B']

        twoA = dist[i][k]['A']
        twoB = dist[i][k]['B']

        threeA = dist[j][k]['A']
        threeB = dist[j][k]['B']

        way1 = twoA + threeA
        way2 = twoA + threeB + transfer[k]
        way3 = twoB + threeA + transfer[k]
        way4 = twoB + threeB
        
        result[i][j] = min(oneA, oneB, way1, way2, way3, way4)


floyd_Warshall()
print(result[1][4])
  