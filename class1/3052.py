ary=[]

for i in range(10):
  num = int(input())
  ary.append(num%42)
  
set1=set(ary)
print(len(set1))