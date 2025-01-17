# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:33:25 2024

@author: dehon
"""
import math

t = int(input())
for _ in range(t):
    n = int(input())
    m = n
    a = sorted(list(map(int, input().split())), reverse = True)
    ans = 0
    if n <= 2:
        print(0)
        continue
    i = 0
    x = 0
    while i < m:
        count = a[i]
        while i < m and a[i] == count:
            x += 1
            i += 1
        n -= x
        if x >= 2:
            ans += math.comb(x, 2) * n
        if x >= 3:
            ans += math.comb(x, 3)
        x = 0
    print(ans)
#    print(ans)

#import math
#from collections import Counter
# 
#t = int(input())
#for _ in range(t):
#    n = int(input())
#    m = n
#    a = Counter(sorted(list(map(int, input().split())), reverse = True))
#    #print(a)
#    ans = 0
#    if n <= 2:
#        print(0)
#        continue
#    for x in a.values():
#        #print(x)
#        n -= x
#        if x >= 2:
#            ans += math.comb(x, 2) * n
#        if x >= 3:
#            ans += math.comb(x, 3)
#        #print(i, count, ans, n)
#    print(ans)