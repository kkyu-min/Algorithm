# 게임 개발

n,m = map(int,input().split())

# 방문한 위치 저장하기 위한 2차원 배열 생성 및 0으로 초기화
visit = [[0]*m for _ in range(n)]

# 현재 위치
x,y,diretion = map(int, input().split())

visit[x][y] = 1
answer=1

# 전체 지도
arr = []

for i in range(n):
  arr.append(list(map(int,input().split())))

#   북 동 남 서 로 방향 설정
dx=[-1,0,1,0]
dy=[0,1,0,-1]


# 왼쪽으로 도는 함수
def turn_left():
  global diretion # global로 함수 바깥에서 선언된 변수
  diretion -=1
  if diretion==-1:
    diretion=3

turn_time=0
while True:
  turn_left()
  nx = x + dx[diretion]
  ny = y + dy[diretion]
  
  if visit[nx][ny]==0 and arr[nx][ny]==0:
    visit[nx][ny]=1
    x=nx
    y=ny
    answer+=1
    turn_time=0
    continue
  else:
    turn_time+=1
  
  if turn_time==4:
    nx = x - dx[diretion]
    ny = y - dy[diretion]
    if arr[nx][ny]==0:
      x=nx
      y=ny
    else:
      break
    turn_time=0
    
print(answer)