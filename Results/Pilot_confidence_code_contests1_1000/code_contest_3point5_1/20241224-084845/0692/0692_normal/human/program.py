#!/usr/bin/env python

while True:
	try:
		n = input()
	except:
		break
	ans = []
	for j in range(10):
		if n & (2 ** j):
			ans.append(str(2 ** j))
	print(" ".join(ans))
