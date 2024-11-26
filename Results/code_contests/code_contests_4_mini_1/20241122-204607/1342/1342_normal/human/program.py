""" ***E-property of Saket Saumya ***
            IIITM

"""
from __future__ import division
from fractions import Fraction
import math
#import os
#import random
#import re
#from sys import stdin, stdout
#from collections import Counter,deque,OrderedDict,defaultdict
#from itertools import permutations,ansduct,combinations
#from heapq import heapify,heappush,heappop,heappushpop,heapify,heapreplace,nlargest,nsmallest
#import numpy as np
#from operator import mul

MOD=10**9+7
INF=float('+inf')

def si():
	return str(stdin.readline())
def ii():
    return int(raw_input())
def mi():
    return map(int, raw_input().split())
def li():
    return [int(i) for i in raw_input().split()]
def debug(x):
	return stdout.write(str(x))
def limul(list):
	return eval('*'.join(str(item) for item in list))

"-----------------------------------------------"
def isPrime(n):
    for i in range(2,int(n**0.5+100)):
        if n%i==0 and n!=i:
            return False
    return True

n=int(input())
if isPrime(n):
    print(1)
elif n%2==0:
    print(2)
elif isPrime(n-2):
    print(2)
else:
    print(3)







#main()
