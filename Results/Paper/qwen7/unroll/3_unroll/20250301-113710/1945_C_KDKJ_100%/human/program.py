from heapq import heappush, heappop, heapify
from collections import defaultdict, deque,Counter
from math import ceil, floor, sqrt, factorial,gcd,cos,sin,pi
from itertools import permutations, combinations,product
from bisect import bisect_left, bisect_right
from copy import deepcopy
from fractions import Fraction
import sys
#from functools import cache,lru_cache #@lru_cache(maxsize=None)
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
vector1 = [[0, -1], [1, 0], [0, 1], [-1, 0]]
vector2 = [[0, 1], [1, 0], [-1, 0], [0, -1],
           [1,-1], [-1, 1], [1, 1], [-1, -1]]
 
 
 
def solve():
    
    n = int(input())
    a = input()
    S = [[0,0]]
    for s in a:
        x, y = S[-1]
        if s == "0":
            x += 1
        else:
            y += 1
        S.append([x,y])
    ans = -1
    for i in range(n+1):
        left = S[i][0]
        lsum = i
        right = S[-1][1] - S[i][1]
        rsum = n - i
        #print(left,right)
        if left*2 < lsum or right*2 < rsum:
            continue
        elif abs(n/2 - i) < abs(n/2 - ans):
                ans = i
        
    print(ans)
    #print(S)
 
    
def main():
    for _ in range(int(input())):
        solve()
    
    
    
    
 
if __name__ == '__main__':
    main()