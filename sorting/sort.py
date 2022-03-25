
arr = [7,5,9,0,3,1,6,2,4,8]

# 선택 정렬(selection sort)

for i in range(len(arr)):
  min_index=i
  for j in range(i+1,len(arr)):
    if arr[min_index] > arr[j]:
      min_index=j
  arr[i],arr[min_index] = arr[min_index],arr[i]
  
print('선택정렬 : ',arr)
#______________________________________

arr = [7,5,9,0,3,1,6,2,4,8]

# 삽입 정렬
# 하나씩 확인하며 적절한 위치에 삽입
# 데이터 정렬시 빠름

for i in range(1,len(arr)):
  for  j in range(i,0,-1):
    if arr[j] < arr[j-1]:
      arr[j],arr[j-1]=arr[j-1],arr[j]
    else:
      break
    
print('삽입정렬 : ',arr)
#______________________________________


arr = [5,7,9,0,3,1,6,2,4,8]

# 퀵 정렬
# 피벗 사용
# 데이터 정렬시 느림

def quick_sort1(array,start,end):
  if  start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right:
      array[right],array[pivot]=array[pivot],array[right]
    else:
      array[left],array[right]=array[right],array[left] 
      
  quick_sort1(arr,start,right-1)
  quick_sort1(arr,right+1,end)

quick_sort1(arr,0,len(arr)-1)
print('퀵정렬1 : ',arr)

arr = [5,7,9,0,3,1,6,2,4,8]

# 파이썬의 장점을 살린 퀵 소트

def quick_sort2(arr):
  if len(arr) <= 1:
    return arr
  
  pivot=arr[0]
  tail=arr[1:]
  
  left_side = [x for x in tail if x<=pivot]
  right_side = [x for x in tail if x>pivot]
  
  return quick_sort2(left_side)+[pivot]+quick_sort2(right_side)
  
print('퀵정렬2 : ',quick_sort2(arr))
#______________________________________


arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 계수 정렬
# 모든 원소의 값이 0보다 크거나 같다고 가정

count = [0] * (max(arr)+1)

for i in range(len(arr)):
  count[arr[i]] += 1
  
print('계수정렬 : ',end='') 
for i in range(len(count)):
  for j in range(count[i]):
    print(i,end=' ')