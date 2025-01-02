'''input
10 5 3 7
.####
###..
##.##
#..#.
.#...
#.##.
.##..
.#.##
#.#..
.#..#
'''
# connected components
from sys import stdin
from collections import defaultdict
import sys
import time

sys.setrecursionlimit(15000)

def calculate_cost(matrix, n, m):
	white_cost = []
	black_cost = []
	for i in range(m):
		bcount = 0; wcount = 0
		for j in range(n):
			if matrix[j][i] == '.':
				bcount += 1
			else:
				wcount += 1
		white_cost.append(wcount)
		black_cost.append(bcount)
	return black_cost, white_cost


def brute(dp1, dp2, matrix, n, m, x, y, black_cost, white_cost, index, w, b):
	#print(index, w, b)
	if index >= m:
		if w != 0 and w >= x:
			return 0
		if b != 0 and b >= x:
			return 0
		return float('inf')
	else:
		if dp1[w][index] != -1 and dp2[b][index] != -1:
			return min(dp1[w][index], dp2[b][index])

		c1 = float('inf'); c2 = float('inf'); c3 = float('inf'); c4 = float('inf')
		if w < x:
			c1 = 0
			cw = w
			i = index
			while cw < x:
				if i == m:
					break
				c1 += white_cost[i]	
				i +=  1; cw += 1
			c1 += brute(dp1, dp2, matrix, n, m, x, y, black_cost, white_cost, i, cw, 0)
		
		if b < x:
			c2 = 0
			cb = b
			i = index
			while cb < x:
				if i == m:
					c2 = float('inf')
					break
				c2 += black_cost[i]
				i += 1; cb += 1
			c2 += brute(dp1, dp2, matrix, n, m, x, y, black_cost, white_cost, i, 0, cb)
		
		if w >= x and w + 1 <= y:
			c3 = white_cost[index] + brute(dp1, dp2, matrix, n, m, x, y, black_cost, white_cost, index + 1, w + 1, 0)
		
		if b >= x and b + 1 <= y:
			c4 = black_cost[index] + brute(dp1, dp2, matrix, n, m, x, y, black_cost, white_cost, index + 1, 0, b + 1)
		
		
		dp1[w][index] = min(c1, c3)
		dp2[b][index] = min(c2, c4)
		return min(c1, c2, c3, c4)
		

# main starts
n, m, x, y = list(map(int, stdin.readline().split()))
matrix = []
for _ in range(n):
	matrix.append(list(stdin.readline().strip()))
black_cost, white_cost = calculate_cost(matrix, n, m)
#print(black_cost, white_cost)
dp1 = [[-1 for j in range(m)] for k in range(y + 1)]
dp2 = [[-1 for j in range(m)] for k in range(y + 1)]

print(brute(dp1, dp2, matrix, n, m, x, y, black_cost, white_cost, 0, 0, 0))
