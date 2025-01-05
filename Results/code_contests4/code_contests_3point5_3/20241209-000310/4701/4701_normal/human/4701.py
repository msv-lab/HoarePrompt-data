import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h,w = map(int, input().split())
ch,cw = map(int, input().split())
dh,dw = map(int, input().split())
ch -= 1
cw -= 1
dh -= 1
dw -= 1
rows,cols = h,w

OK = "."
NG = "#"

from collections import defaultdict

ns = defaultdict(set)
ss = [None] * rows
for i in range(rows):
    s = input()
    ss[i] = s
n = rows * cols
start = ch*w+cw
goal = dh*w+dw
seen = [None]*n
seen[start] = 0
from heapq import heappop as hpp, heappush as hp
q = [(0, start)] # ワープ回数, 現在位置, 最後の道の位置
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
dx = []
dy = []
vvs = []
for i in range(-2,3):
    for j in range(-2,3):
        if not (i==j==0):
            dx.append(i)
            dy.append(j)
            if abs(i)+abs(j)>1:
                vvs.append(1)
            else:
                vvs.append(0)
while q:
    pnum,pu = hpp(q)
    ux,uy = divmod(pu,w)
    # print(pnum,divmod(pu,w))
    if pu==goal:
        break
    for xx,yy,vv in zip(dx,dy,vvs):
#         x = ux+xx
#         y = uy+yy
        x,y = ux+xx, uy+yy
        u = x*w + y
        num = pnum+vv
        if x<0 or y<0 or x>=h or y>=w or ss[x][y]=="#":
            continue
#         print(x,y)
        if seen[u] is None or seen[u]>num:
            seen[u] = num
            hp(q, (num, u))
val = seen[goal]
if val is None:
    print(-1)
else:
    print(val)