#!/usr/local/bin/python

# 

import math
import sys

table = {
	'>':8,
	'<':9,
	'+':10,
	'-':11,
	'.':12,
	',':13,
	'[':14,
	']':15
}

input = sys.stdin.readline().rstrip()

prev = 0
for c in input:
	s = "{0:0>{1}}".format(bin(ord(c))[2:], 8)
	binary = s[::-1]
	integer = int(binary, 2)
	print (prev - integer) % 256
	prev = integer
