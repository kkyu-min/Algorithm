# 숫자 카드 게임

# 책 풀이 
n,m = map(int,input().split())
answer=0

for i in range(n):
  data = list(map(int,input().split()))
  min_value=min(data)
  answer=max(answer,min_value)

print(answer)
# 내 풀이

# n,m = map(int,input().split())
# answer=0

# for i in range(n):
#   data = list(map(int,input().split()))
#   min_value = 10001
#   for j in data:
#     min_value=min(min_value,j)
#   answer=max(answer,min_value)
  
# print(answer)