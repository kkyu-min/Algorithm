# 1이 될때까지

# 내 풀이
n,k = map(int,input().split())
count=0

while n!=1:
  if n%k==0:
    n/=k
    count+=1
    print(n)
  else:
    n-=1
    count+=1
    print(n)

print(count) 