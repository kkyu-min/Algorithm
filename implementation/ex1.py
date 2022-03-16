# 구현 예제1
# 상하좌우

# 내 풀이
# n = int(input())
# ways=list(map(str,input().split()))
# x,y=1,1

# for way in ways:
#   if way=='D':
#     if x<n:
#       x+=1
#   elif way=="U":
#     if x>1:
#       x-=1
#   elif way=="L":
#     if y>1:
#       y-=1
#   elif way=="R":
#     if y<n:
#       y+=1
#   print(x,y)
     
# print("----") 
# print(x,y)

# 책 풀이

n = int(input())
plans=input().split()
x,y=1,1

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      rx=x+dx[i]
      ry=y+dy[i]
  if rx<1 or rx>n or ry<1 or ry>n:
    continue
  x,y=rx,ry
  
print(x,y)