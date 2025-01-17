for ii in range(int(input())):
  n,k,m = map(int,input().split())
  s = input()
  t = 0
  c = 0
  f = {}
  r = ""
  for i in range(m):
    if s[i] not in f:
      t+=1
      f[s[i]] = 1
    if t==k:
      r+=s[i]
      c+=1
      t = 0
      f = {}
    if c==n:
      print("YES")
      break
  if c<n:
    for i in range(k):
      if chr(ord("a")+i) not in f:
        r+=chr(ord("a")+i)
        break
    e = n-len(r)
    for i in range(e):
      r+="a"
    print("NO")
    print(r)
    
      