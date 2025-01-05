def cake(n,x,a):
  res=x-2
  a.sort()
  for i in range(x-1):
    if a[i+1]-a[i]==2:
      res+=1
  if a[-1]==n-1 and a[0]==1:
    res+=1
  return res

t=int(input())
for _ in range(t):
  [n,x,y]=list(map(int,input().split()))
  a=list(map(int,input().split()))
  print(cake(n,x,a))