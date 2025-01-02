from sys import stdin, stdout
from collections import Counter, defaultdict
from itertools import permutations, combinations
raw_input = stdin.readline
pr = stdout.write
mod=10**9+7

def ni():
    return int(raw_input())


def li():
    return map(int,raw_input().split())


def pn(n):
    stdout.write(str(n)+'\n')


def pa(arr):
    pr(' '.join(map(str,arr))+'\n')

# fast read function for total integer input

def inp():
    # this function returns whole input of
    # space/line seperated integers
    # Use Ctrl+D to flush stdin.
    return map(int,stdin.read().split())

range = xrange # not for python 3.0+

#main code

n=ni()
BITTree=[0]*(n+1)
def gs(i): 
    s = 0
    i = i+1
    while i > 0:  
        s += BITTree[i] 
        i -= i & (-i) 
    return s 
def ub(i ,v): 
    i += 1
    while i <= n: 
        BITTree[i] += v 
        i += i & (-i) 
def fun(x):
    ret=0
    sm=0
    for i in range(21,-1,-1):
        pw=1<<i
        if ret+pw<=n and sm+BITTree[ret+pw]<=x:
            ret+=pw
            sm+=BITTree[ret]
    return ret
l=li()
for i in range(n):
    ub(i,i)
ans=[0]*n
for i in range(n-1,-1,-1):
    ans[i]=fun(l[i])
    ub(ans[i],-ans[i])
pa(ans)

    
