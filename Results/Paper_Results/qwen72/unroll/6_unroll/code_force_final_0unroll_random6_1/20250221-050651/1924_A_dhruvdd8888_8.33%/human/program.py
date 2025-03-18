from collections import *
from math import *
from heapq import *
import sys
from bisect import *
from random import randint
rrr = randint(8888,88888)
 
 
def sol():
    n,k,m = tuple(map(int,input().split()))
 
    s = input()
    us = set(chr(i+97) for i  in range(k))
    win = set()
    ans = []
    ps = 0
    for i in s:
        if i in us:
            win.add(i)
            if len(win) == k:
                ans.append(i)
                ps += 1
                win.clear()
    
    # print(ps)
    if ps >= n:return print("YES")
 
    print("NO")
 
    for i in  us:
        if i not in win:
            print("".join(ans)+i + ("a" * (n - len(ans) - 1)))
 
 
 
for _ in range(int(input())):
    sol()