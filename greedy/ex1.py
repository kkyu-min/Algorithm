# 그리디 알고리즘 예제1
# 정당성 분석이 중요

sum = int(input())
count = 0

# 큰 단위부터 확인 
coin_types=[500,100,50,10]

for coin in coin_types:
  count += sum//coin # 제일 큰 값부터 주기 위함
  sum%=coin

print(count) 