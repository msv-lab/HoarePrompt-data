# https://vjudge.net/contest/338364#problem/B
from math import ceil

n = int(input())
nums = list(map(int, raw_input().split(' ')))
cond = round(n / 2.0)
positives = set()
negatives = set()
p1 = 0
n1 = 0
for i in nums:
    if i > 0:
        p1 += 1
    if i < 0:
        n1 += 1

if p1 < cond and n1 < cond:
    print(0)
elif p1 >= cond:
    print(4)
else:
    print(-4)
	 	 				  	   		 	   	  				