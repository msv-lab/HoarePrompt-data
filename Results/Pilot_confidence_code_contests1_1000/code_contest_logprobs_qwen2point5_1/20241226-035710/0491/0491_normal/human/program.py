from __future__ import division;
from bisect import *;
from fractions import Fraction;
import sys;
from math import *;
from fractions import *;
import io;
import re;

INF = 987654321987654321987654321;

def readint(delimiter=' ') :
	return map(int, raw_input().split(delimiter));

def readstr(delimiter=' ') :
	return raw_input().split(delimiter);

def readfloat(delimiter=' ') :
	return map(float, raw_input().split(delimiter));

def index(a, x):
	'Locate the leftmost value exactly equal to x'
	i = bisect_left(a, x)
	if i != len(a) and a[i] == x:
		return i
	raise ValueError

def find_lt(a, x):
	'Find rightmost value less than x'
	i = bisect_left(a, x)
	if i:
		return a[i-1]
	raise ValueError

def find_le(a, x):
	'Find rightmost value less than or equal to x'
	i = bisect_right(a, x)
	if i:
		return a[i-1]
	raise ValueError

def find_gt(a, x):
	'Find leftmost value greater than x'
	i = bisect_right(a, x)
	if i != len(a):
		return a[i]
	raise ValueError

def find_ge(a, x):
	'Find leftmost item greater than or equal to x'
	i = bisect_left(a, x)
	if i != len(a):
		return a[i]
	raise ValueError

def bin_search(a, x, left, right) :

	while left<=right :
		mid = (left + right)//2;
		
		if a[mid] == x :
			return mid;
		elif a[mid] < x :
			left = mid + 1; 
		elif a[mid] > x :
			right = mid - 1;
					   
		pass
	
	return -1;
	pass

def printf(format, *args):
	"""Format args with the first argument as format string, and write.
	Return the last arg, or format itself if there are no args."""
	sys.stdout.write(str(format) % args)
	

from datetime import date;

if __name__ == '__main__':

	a, b, c, d = readint();

	prob_a = a/b;
	prob_b = c/d;

	prev = 0;
	now = 0;
	now += prob_a;
	acc = (1-prob_a)*(1-prob_b);
	ii = 0;
	while (now - prev > 0.0000001) :
		prev = now;
		ii += 1;
		now += acc*prob_a;
		acc *= (1-prob_a)*(1-prob_b);
		pass

	printf('%.6f\n', now);
	
	pass