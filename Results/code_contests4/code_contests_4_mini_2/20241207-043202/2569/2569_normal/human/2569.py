 ######      ###      #######    #######    ##      #     #####        ###     ##### 
 #     #    #   #          #        #       # #     #    #     #      #   #     ###  
 #     #   #     #        #         #       #  #    #   #       #    #     #    ###  
 ######   #########      #          #       #   #   #   #           #########    #   
 ######   #########     #           #       #    #  #   #           #########    #   
 #     #  #       #    #            #       #     # #   #    ####   #       #    #   
 #     #  #       #   #             #       #      ##   #    #  #   #       #        
 ######   #       #  #######     #######    #       #    #####  #   #       #    #   

from __future__ import print_function # for PyPy2
from collections import Counter, OrderedDict
from itertools import permutations as perm
from fractions import Fraction
from collections import deque
from sys import stdin
from bisect import *
from heapq import *
import math
 
g   = lambda : stdin.readline().strip()
gl  = lambda : g().split()
gil = lambda : [int(var) for var in gl()]
gfl = lambda : [float(var) for var in gl()]
gcl = lambda : list(g())
gbs = lambda : [int(var) for var in g()]
mod = int(1e9)+7
inf = float("inf")

n, m, a = gil()
person, bikes = gil(), gil()
person.sort()
bikes.sort()

def isPos(k):
	left = a
	b = 0
	for i in range(k):
		pi = -k+i
		left -= max(0, bikes[i]-person[pi])	
		b += min(person[pi], bikes[i])

	b -= left
	return b, left


k, cost = 0, 0	
l, r = 0, min(n, m)

while l <= r:
	mid = (l+r)//2
	cost_, left = isPos(mid)
	if left >= 0:
		l = mid + 1
		k = mid
		cost = cost_
	else:
		r = mid - 1


print(k, max(0, cost))