'''input
5 1000000000
6 6 2 6 2
'''
# A coding delight
from sys import stdin, stdout
import gc
from copy import deepcopy
from itertools import permutations
gc.disable()
input = stdin.readline
import math


def myfunc(num):
	return num//2

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a%b)
	

def find_lcm(num1, num2): 
    return (num1 * num2) // gcd(num1, num2)

def lcm(l):
	if len(l) == 1:
		return l[0]
	num1 = l[0] 
	num2 = l[1] 
	lcm = find_lcm(num1, num2) 
	  
	for i in range(2, len(l)): 
	    lcm = find_lcm(lcm, l[i])
	return lcm
# main starts
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr = list(map(myfunc, arr))
num = lcm(arr)


aux = num
while aux % 2 == 0:
	aux //= 2

if aux == 0:
	num *= 3

# print(num)
if num > m:
	print(0)
else:
	k = m//num
	if k % 2 == 0:
		print(k//2)
	else:
		print(k//2 + 1)
	
