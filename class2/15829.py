length = int(input())
hashstr = list(map(str,input()))

sum=0

for i in range(length):
  tmp = (31 ** i)
  tmp *= int(ord(hashstr[i])-96)
  sum += tmp

if sum >=1234567891:
  print(sum%1234567891)
else:
  print(sum)