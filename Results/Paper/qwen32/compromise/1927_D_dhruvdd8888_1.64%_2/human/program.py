from collections import *
from math import log,log2,pow,gcd,ceil,floor
from heapq import *
import sys
from bisect import *
 
def sol():
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int,input().split()))
    s = 0
    e = 0
    num = nums[0]
    arr = []
    nums.append(-1)
    for i in range(N+1):
        if nums[i] != num:
            arr.append((1+s,i,num))
            s = i
        
        num = nums[i]
    # print(nums)
    # print(arr)
    LA = len(arr)-1
    if ppp == 23:print(nums)
    for _ in range(int(input())):
        l,r = tuple(map(int,input().split()))
        if tc > 5:
            if ppp == 23:
                print(l,r)
            continue
        eli = bisect_left(arr,(l,0,0))
        # if eli >= LA:s,e,_ = arr[-1]
        s,e,_ = arr[min(eli,LA)]
        # print(arr[bisect(arr,(l,0,0))])
        # print(l,r ,end = "   = ")
        if s > l:
            if s == 1:print(-1,-1)
            else:print(s-1,s)
        elif e >= r:print(-1,-1)
        else:
            if e < N:print(s,e+1)
            else:print(-1,-1)
        
    # print()    
 
tc= int(input())
 
 
for ppp in range(tc):
    sol()