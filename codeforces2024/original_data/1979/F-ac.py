q=lambda d: print("? %d" % d, flush=True) or map(int, (input().split()))
for _ in range(int(input())):
 vx, ops = set(i for i in range(1, int(input())+1)), []
 while(len(vx) > 2):
  v1, v2 = q(len(vx)-2)
  vx.remove(v1)
  if v2 > 0: ops+=[(v1, v2)]
  else:
   v3, _ = q(0)
   vx.remove(v3)
   ops += [(v3,0),(v1,0)]
 p1, p2 = list(vx), []
 for v1, v2 in ops[::-1]:(p2 if p1[-1] == v2 else p1).append(v1)
 print("! %s" % ' '.join(map(str,p1[::-1] + p2)), flush=True)