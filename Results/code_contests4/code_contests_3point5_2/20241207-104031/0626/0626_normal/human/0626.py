#!/usr/bin/python

import sys
import math 
import re
from datetime import datetime

sys.setrecursionlimit(20000)
startTime = datetime.now()

def readn(n):
    return [raw_input().strip() for i in range(n)]
def read():
    return raw_input().strip()
def readints():
    return map(int, read().split())
def readint():
    return readints()[0]
def wl(o):
    print(o)

def GCD(a,b):
    while b!=0:
        a %= b;
        a,b = b,a
    return a
    
def LCM(a,b):
    return (a / GCD(a,b)) * b;
    
def SetParent(node, parent):
    ii = -1
    for i in range(len(node[2])):
        
        if node[2][i] != parent:
            SetParent(node[2][i], node)
        else:
            ii = i
    if ii >= 0: node[2].pop(ii)
        
def Calc(node):
    if node[1] >= 0: return
    
    lcm = 1
    max = -1
    for child in node[2]:
        Calc(child)
        lcm = LCM(lcm, child[0])
    for child in node[2]:
        t = (child[1] / lcm) * lcm
        if max < 0 or max > t:
            max = t
    node[0] = lcm
    node[1] = max * len(node[2])
    
n=readint()
sum = 0
ar = [0] * n
xx = readints()
for i in range(len(xx)):
    x = xx[i]
    if x == 0:
        ar[i] = [1, -1, []]
    else:
        ar[i] = [1, x, []]
    sum += x
for i in range(n-1):
    x, y = readints()
    x -= 1
    y -= 1
    ar[x][2].append(ar[y])
    ar[y][2].append(ar[x])
    
SetParent(ar[0], [])
Calc(ar[0])
wl(sum - ar[0][1])


#print(datetime.now()-startTime)