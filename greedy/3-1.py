# 큰수의 법칙

# 책 풀이 -1
# n,m,k = map(int, input().split())
# ary = list(map(int,input().split()))

# ary.sort(reverse=True)
# answer=0

# while True:
#   for i in range(k):
#     if m==0:
#       break
#     answer+=ary[0]
#     m-=1
#   if m==0:
#     break
#   answer+=ary[1]
#   m-=1

# print(answer)

# 책 풀이 -2
n,m,k = map(int, input().split())
ary = list(map(int,input().split()))

ary.sort()
first=ary[n-1]
second=ary[n-2]

# 가장 큰수가 더해지는 횟수
count = int(m/(k+1)) * k
count += m%(k+1)

answer=0
answer += count*first # 가장 큰수 더하기
answer += (m-count)*second # 두번째로 큰수 더하기


# 내 풀이 
# n,m,k = map(int, input().split())
# ary = list(map(int,input().split()))
# answer=0
# count=1

# ary.sort(reverse=True)

# for i in range(m):
#   if count<k:
#     count+=1
#     answer+=ary[0]
#   elif count==k:
#     answer+=ary[0]
#     count+=1
#     print(count)
#   else:
#     answer+=ary[1]
#     count=1
  
    
# print(answer)