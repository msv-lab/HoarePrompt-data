"""
Author    : raj1307 - Raj Singh
Institute : Jalpaiguri Government Engineering College
Date      : 18.04.19
"""
from __future__ import division, print_function
import itertools,os,sys,threading
from collections import deque, Counter, OrderedDict, defaultdict
#from heapq import nsmallest, nlargest, heapify, #heappop ,heappush, heapreplace
#from math import ceil,floor,log,sqrt,factorial,pow,pi
#from bisect import bisect_left,bisect_right
#from decimal import *






def ii(): return int(input())
def si(): return str(input())
def mi():return map(int,input().strip().split(" "))
def li():return list(mi())

abc='abcdefghijklmnopqrstuvwxyz'
abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
def getKey(item): return item[0] 
def sort2(l):return sorted(l, key=getKey)
def d2(n,m,num):return [[num for x in range(m)] for y in range(n)]
def ntl(n):return [int(i) for i in str(n)]
def powerMod(x,y,p):
    res = 1
    x %= p
    while y > 0:
        if y&1:
            res = (res*x)%p
        y = y>>1
        x = (x*x)%p1
    return res
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# For getting input from input.txt file 
#sys.stdin = open('input.txt', 'r')  
  
# Printing the Output to output.txt file 
#sys.stdout = open('output.txt', 'w') 

vis=[0]*1000000
col=[0]*1000000
def dfs(u,c):
    
    if vis[u]:
        if col[u]!=c:
            print('NO')
            exit()
        return
    col[u]=c
    vis[u]=1
    for i in g[u]:
        dfs(i,c^1)
    
g=defaultdict(list)

def main():
   
    n,m=mi()
    uu=[0]*1000000
    for i in range(m):
        x,y=mi()
        uu[i]=x
        g[x].append(y)
        g[y].append(x)
        
    dfs(1,0)
    print('YES')
    for i in range(m):
        if col[uu[i]]:
            print(1,end='')
        else:
            print(0,end='')
    
    
    

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    threading.stack_size(20480000)
    thread = threading.Thread(target=main)
    thread.start()