str = list(map(str,input()))

for i in range(97,123):
  for j in range(len(str)):
    tmp = -1
    if chr(i)==str[j]:
      tmp=j
      break
  print(tmp,end=" ")