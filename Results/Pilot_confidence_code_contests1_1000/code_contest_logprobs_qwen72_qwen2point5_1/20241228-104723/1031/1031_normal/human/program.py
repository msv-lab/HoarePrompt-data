"""
Author    : raj1307
Institute : Jalpaiguri Government Engineering College
Date      : 21.03.19
"""
from __future__ import division, print_function
import itertools,os,sys
#from collections import deque, Counter, OrderedDict
#from heapq import nsmallest, nlargest, heapify, #heappop ,heappush, heapreplace
#from math import ceil,floor,log,sqrt,factorial,pow,pi
#from bisect import bisect_left,bisect_right
#from decimal import *
from atexit import register
from io import BytesIO, StringIO

if sys.version_info[0]<3:
    range = xrange
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
    sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
    sys.stdout = BytesIO()
    register(lambda: os.write(1, sys.stdout.getvalue()))
else:
    sys.stdin = StringIO(os.read(0, os.fstat(0).st_size).decode())
    sys.stdout = StringIO()
    register(lambda: os.write(1, sys.stdout.getvalue().encode()))

input = lambda: sys.stdin.readline().rstrip('\r\n')

def ii(): return int(input())
def si(): return str(input())
def mi():return map(int,input().strip().split(" "))
def li():return list(mi())

abc='abcdefghijklmnopqrstuvwxyz'
abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
def getKey(item): return item[0] 
def sort2(l):return sorted(l, key=getKey)
def d2(n,num):return [[num for x in range(n)] for y in range(n)]
def ntl(n):return [int(i) for i in str(n)]
def powerMod(x,y,p):
    res = 1
    x %= p
    while y > 0:
        if y&1:
            res = (res*x)%p
        y = y>>1
        x = (x*x)%p
    return res
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def main():
    n=ii()
    l=si()
    cnt=0
    for i in range(n):
        if int(l[i])%2==0:
            cnt+=i+1
    
    print(cnt)
   
if __name__ == "__main__":
    main()