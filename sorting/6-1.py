# 위에서 아래로

n=int(input())

arr=[]

for i in range(n):
  arr.append(int(input()))
  
arr = sorted(arr, reverse=True)

for i in range(n):
  print(arr[i],end=" ")