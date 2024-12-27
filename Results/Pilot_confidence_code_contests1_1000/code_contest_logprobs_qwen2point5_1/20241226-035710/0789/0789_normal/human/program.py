from math import *
from Queue import *
from sys import *







n, t = map(int, raw_input().split())
B = []
for i in range(n):
    x, v, m = map(int, raw_input().split())
    B.append([x, v, m, i])
B.sort()
curTime = 0
while curTime < t:
    nextCol = t+1
    b = n
    for i in range(n-1):
        s = B[i][1] - B[i+1][1]
        if (s > 0) and (nextCol > float(B[i+1][0] - B[i][0])/s):
            nextCol = float(B[i+1][0] - B[i][0])/s
            b = i
    if curTime + nextCol >= t:
        break
    else:
        curTime += nextCol
        for i in range(n):
            B[i][0] += nextCol*B[i][1]
        B[b][1], B[b+1][1] = float((B[b][2] - B[b+1][2])*B[b][1] + 2*B[b+1][2]*B[b+1][1])/(B[b][2] + B[b+1][2]), float((B[b+1][2] - B[b][2])*B[b+1][1] + 2*B[b][2]*B[b][1])/(B[b][2] + B[b+1][2])
for i in range(n):
    B[i][0] += (t - curTime)*B[i][1]
for i in range(n):
    for b in B:
        if b[3] == i:
            print(b[0])
            break
