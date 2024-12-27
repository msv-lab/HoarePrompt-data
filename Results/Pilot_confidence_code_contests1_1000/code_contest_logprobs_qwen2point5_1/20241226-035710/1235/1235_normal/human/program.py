from sys import maxint, stdin, stdout
import os
from io import BytesIO
stdin = BytesIO(os.read(0, os.fstat(0).st_size))
stdout = BytesIO()
input = stdin.readline
write = lambda x: os.write(1, x)

res = []
T = int(input())
for t in range(T) :
  N = int(input())

  monsters = []
  mnShots = 0
  start = float('inf')

  for n in range(N) : monsters.append(map(int,input().split()))
  for n in range(N) :
    cur = monsters[n]
    dam = max(0,cur[0] - monsters[n-1][1])
    mnShots += dam
    start = min(start, cur[0]-dam) 

  res.append(mnShots + start)

write('\n'.join(str(x) for x in res))

  
