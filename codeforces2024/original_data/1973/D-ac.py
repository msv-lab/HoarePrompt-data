for i in range(int(input())):
  n,k=map(int,input().split())
  for j in range(n,0,-1):
    print("?",1,j*n,flush=True)
    if int(input())==n:
      x=j
      break
  v=True
  for j in range(n//k,0,-1):
    count=0
    m=j*x
    r=1
    while r!=n+1:
      print("?",r,m,flush=True)
      r=int(input())
      if r!=n+1:
        count+=1
        r+=1
      else:
        count=0
        break
    if count==k:
      print("!",m,flush=True)
      v=False
      break
  if v:
    print("!",-1)
  input()