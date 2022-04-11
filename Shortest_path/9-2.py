# 전보

n,m,start=map(int,input().split())

graph = [[] for i in range(n+1)]
distance

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))