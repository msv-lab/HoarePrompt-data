# coding: utf-8

import math

n = int(raw_input())

for i in range(n):
	data = map(float, raw_input().split())
	x1 = data[0]
	y1 = data[1]
	x2 = data[2]
	y2 = data[3]
	x3 = data[4]
	y3 = data[5]

	k = 0.5 * ( (x3-x2)*(x3-x1) + (y3-y2)*(y3-y1) ) / ( (x2-x1)*(y3-y1) + (y2-y1)*(x3-x1) )

	x = 0.5 * (x1 + x2) - k * (y2 - y1)
	y = 0.5 * (y1 + y2) + k * (x2 - x1)

	r = math.sqrt( (x-x1)**2 + (y-y1)**2 )

	print("{:.3f} {:.3f} {:.3f}".format(x,y,r))