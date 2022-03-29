# 떡볶이 떡 만들기


import re


n,m = map(int,input().split())

length=list(map(int,input().split()))

start = 0
end = max(length)
result = 0

while start <= end:
  total = 0
  mid = (start+end) //2
  for i in length:
    if i > mid:
      total += i-mid
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
    
print(result)