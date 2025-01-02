import sys
import math

if sys.subversion[0] == "PyPy":
    import io, atexit

    sys.stdout = io.BytesIO()
    atexit.register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))

    sys.stdin = io.BytesIO(sys.stdin.read())
    input = lambda: sys.stdin.readline().rstrip()

#t = int(raw_input())

# python codesforces210710.py < input.txt
#for zz in range(t):

str1 = raw_input().split(' ')
n, r1, r2, r3, d = map(int, str1)
str2 = raw_input().split(' ')
a = map(int, str2)
fs = 0
c1 = 0
c2 = 2 * d

for i in range(n):
    #print(aii)
    indcost = r3 + a[i] * r1
    aoecost = min(r2 + r1, r1 * (a[i] + 2))
    mincost = min(indcost, aoecost)
    mincost2l = min(indcost - d, aoecost)
    oto = indcost
    ott = mincost + 2 * d
    ttt = mincost + 2 * d
    tto = mincost
    #print(oto, ott, ttt, tto)
    if i < n - 1:
        c3 = min(c1 + oto, c2 + tto) + d
        c4 = min(c1 + ott, c2 + ttt) + d
    else:
        c3 = min(c1 + oto, c2 + mincost2l) + d
        c4 = min(c1 + ott, c2 + ttt) + d
    c1 = c3
    c2 = c4
    #print(c1, c2)
ans = min(c1, c2) - d
print(ans)
