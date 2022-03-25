# 성적이 낮은 순서로 학생 출력하기

num = int(input())

arr = []

for i in range(num):
  input_data=input().split()
  arr.append((input_data[0],int(input_data[1])))


arr = sorted(arr, key=lambda student: student[1])

for student in arr:
  print(student[0],end=" ")