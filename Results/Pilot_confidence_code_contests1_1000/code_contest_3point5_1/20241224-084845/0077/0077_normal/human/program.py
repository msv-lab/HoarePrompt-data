from sys import stdin, stdout
from collections import Counter, defaultdict
from itertools import permutations, combinations
raw_input = stdin.readline
pr = stdout.write


def in_num():
    return int(raw_input())


def in_arr():
    return map(int,raw_input().split())


def pr_num(n):
    stdout.write(str(n)+'\n')


def pr_arr(arr):
    pr(' '.join(map(str,arr))+'\n')

# fast read function for total integer input

def inp():
    # this function returns whole input of
    # space/line seperated integers
    # Use Ctrl+D to flush stdin.
    return map(int,stdin.read().split())

range = xrange # not for python 3.0+

# main code

n,k,p=in_arr()
a=in_arr()
b=in_arr()
a.sort()
b.sort()
ans=1000000000000
for i in range(k-n+1):
    temp=0
    for j in range(n):
        temp=max(temp,int(abs(b[i+j]-a[j])+abs(b[i+j]-p)))
    ans=min(ans,temp)
pr_num(ans)
