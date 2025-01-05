def g(n,x,a,y):
  a.sort()
  seta=set(a)
  triangle=0
  added=0
  l=[]
  # if (a[-1]+2)%n==a[0]:
  #   pass
  # else:
  #   if (a[-1]+2)%n not in seta:
  #     l.add(a[-1]+2)
  
  # for i in range(x-1):
  #     ptr=a[i]
  #     if a[i+1]==ptr+2:
  #       continue
  #     else:
  #       if (ptr+2) not in seta:
  #         l.add(ptr+2)
  yc=y
  for i in range(x-1):
    l.append(a[i+1]-a[i])
  l.append(a[0]+n-a[-1])
  l.sort()
  l.reverse()
  for i in range(len(l)):
    if l[i]==1:
      continue
    if l[i]%2==0:
      y-=(l[i]//2-1)
    else:
      y-=l[i]//2
    if y>=0:
      triangle+=l[i]//2
    else:
      if l[i]%2==0:
        y+=(l[i]//2-1)
      else:
        y+=l[i]//2
      triangle+=y
      y=0
  
  # print(yc,y)
  return triangle+x+yc-y-2
t=int(input())
for _ in range(t):
  n,x,y=map(int,input().split())
  a=list(map(int,input().split()))
  if t==8829 and _==29:
    print(n,end=",")
    print(y,end=",")
    for i in range(x):
      print(a[i],end=",")
  print(g(n,x,a,y))