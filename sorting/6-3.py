# 두 배열의 원소 교체

n,k =map(int,input().split())

arr_a=list(map(int,input().split()))
arr_b=list(map(int,input().split()))


arr_a=sorted(arr_a)
arr_b=sorted(arr_b,reverse=True)

for i in range(k):
  if arr_a[i] < arr_b[i]:
    arr_a[i],arr_b[i]=arr_b[i],arr_a[i]
  else:
    break
    

  
print(sum(arr_a))