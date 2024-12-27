n=input()
a=[0]+map(int,raw_input().split())
b=[a[a[x]] for x in range(n+1)]
t=200
for x in range(1,n+1):
  if a[x]!=x:
    u=x
    v=[0]*111
    z=0
    while not v[u]:
      v[u]=1
      u=b[u]
      z+=1
    if u==x:
      t=min(t,z)
print -1 if t>100 else t
