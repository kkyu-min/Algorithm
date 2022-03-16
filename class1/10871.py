num, x = map(int, input().split())

ary = list(map(int, input().split()))

for i in range(num):
  if ary[i]<x:
    print(ary[i],end=" ")
  