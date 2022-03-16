# 왕실의 나이트

loc=input()

row=int(loc[1])
col=int(ord(loc[0]))-int(ord('a')) + 1

answer=0

move_types = [(-2,-1),(-2,1),(2,-1),(2,1),(1,-2),(1,2),(-1,-2),(-1,2)]

for move in move_types:
  next_row = row + move[0]
  next_col = col + move[1]
  if next_row <= 8 and next_row >= 1 and next_col >= 1 and next_col <= 8:
    answer+=1

print(answer)  