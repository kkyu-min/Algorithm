# 재귀 함수로 구현한 이진 탐색

def binary_search1(arr,target,start,end):
  if start > end:
    return None
  mid=(start+end)//2
  
  if arr[mid] == target:
    return mid
  elif arr[mid] < target:
    return binary_search1(arr,target,mid+1,end)
  else:
    return binary_search1(arr,target,start,end-1)
  
  
n, target = list(map(int,input().split()))

arr = list(map(int,input().split()))

arr = sorted(arr)

result1 = binary_search1(arr,target,0,n-1)

if result1 == None:
  print("존재하지 않습니다.")
else:
  print(result1+1)
  
# 반복문으로 구현한 이진 탐색

def binary_search2(arr,target,start,end):
  while start <= end:
    mid = (start+end) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      start = mid +1
    else:
      end = mid - 1
  return None


result2 = binary_search1(arr,target,0,n-1)

if result2 == None:
  print("존재하지 않습니다.")
else:
  print(result2+1)
  
# 빠르게 입력받기
import sys

input_data = sys.stdin.readline().rstrip()

print(input_data)