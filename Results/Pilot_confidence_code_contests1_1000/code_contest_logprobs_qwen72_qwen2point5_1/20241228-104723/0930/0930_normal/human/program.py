import math
n =int(raw_input())
l = list(map(int,raw_input().split()))
zero = l.count(0)
for i in range(n):
  r = round(math.sqrt(l[i]))
  l[i] = abs(l[i]-r*r) 
l.sort()
rzero = max(0,zero-n//2)
print(sum(l[0:n//2]) + rzero*2 + l[n//2:n].count(0)-rzero)