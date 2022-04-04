# 플로이드 워셜 알고리즘

import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력 받기
n = int(input())
m = int(input())
# 2차원  리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j:
      graph[i][j]=0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # a에서 b로 가는 비용을 c
  a,b,c=map(int,input().split())
  graph[a][b]=c
  
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,n+1):
      graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])


for i in range(1,n+1):
  for j in range(1,n+1):
    # 도달할 수 없는 경우, 무한으로 출력
    if graph[i][j]==INF:
      print("무한",end=' ')
    else:
      print(graph[i][j],end=' ')
  print()