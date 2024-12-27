#!/usr/bin/python

import sys
import math 
import re
from datetime import datetime
from decimal import *

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

#print(datetime.now()-startTime)
NP = readints()
N = NP[0]
P = NP[1:]

minD = 1000000000000000000;
maxD = 0;

for i in range(N):
    X = readints()
    d = (P[0] - X[0]) * (P[0] - X[0]) + (P[1] - X[1]) * (P[1] - X[1]);
    minD = min(minD, d);
    maxD = max(maxD, d);

print +Decimal(math.pi)*(maxD-minD)