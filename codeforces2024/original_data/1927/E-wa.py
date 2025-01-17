from math import *
a = int(input())
for _ in range(a):
  b,c = map(int,input().split())
  h = ceil(b/c)
  s = b
  m = 0
  o  = []
  f = 0
  l = 0
  for y in range(b):
    
    if y%c == 0:
      f = 0
      s = b-m
      m += 1
      l = h
      o.append(s)
    else:
      s -= l
      o.append(s)
      if l%2 == 0:
        if f >= 0:
          if l > 2:
            l -= 1
            
          f = 0
      
        else:
          f += 1
      else:
        if f >= 1:
          if l > 2:
            l -= 1
          f = 0
      
        else:
          f += 1
      
      
  print(*o)