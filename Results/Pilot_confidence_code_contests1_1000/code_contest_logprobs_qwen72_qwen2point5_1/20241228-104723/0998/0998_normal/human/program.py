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
temp=[2**i for i in range(31)]
for t in range(input()):
    n=input()
    
    ans=2
    n/=2
    #n-=1
    for i in range(1,n):
        ans+=2*temp[i]
    pr_num(ans)
