# 부품 찾기

# 내 풀이 & 이진 탐색 풀이
# def binary_search(arr,target,start,end):
#   while start <= end:
#     mid = (start+end)//2
#     if arr[mid]==target:
#       return True
#     elif arr[mid] < target:
#       start = mid + 1
#     else:
#       end = mid - 1
#   return False

          
# n=int(input())
# arr= list(map(int,input().split()))

# arr= sorted(arr)

# m=int(input())
# find=list(map(int,input().split()))

# find = sorted(find)

# for i in range(m):
#   result = binary_search(arr,find[i],0,n-1)
#   if result == True:
#     print("yes",end=' ')
#   else:
#     print("no",end=' ')
    
# 계수 정렬

# n = int(input())
# arr = [0] * 1000001

# for i in input().split():
#   arr[int(i)] = 1
  
# m = int(input())

# find = list(map(int,input().split()))

# for i in find:
#   if arr[i] == 1:
#     print('yes',end=' ')
#   else:
#     print('no',end=' ')


# 집합 자료형 사용 

n = int(input())

arr=set(map(int,input().split()))

m = int(input())
find = list(map(int,input().split()))

for i in find:
  if i in arr:
    print("yes",end=' ')
  else:
    print("no",end=' ')