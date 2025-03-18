a='abcdefghijklmnopqrstuvwxyz'
 
for t in range(int(input())):
  b=[0]*26
  n=int(input())
  s=list(map(int,input().split()))
  r=''
  for i in s:
    
    x=b.index(i)
  
    r+=a[x]
    b[x]+=1
  print(r)