# a, b, c, d = [int (x) for x in input().split()]

import sys 
input = sys.stdin.readline

from collections import defaultdict



def solve():
	n = int(input())
	a = list(map(int, input().split()))
	flag = True
	for i in range(1, n-1):
		left = a[i-1] if a[i-1] <= n // 2 else n - a[i-1] + 1
		right = a[i+1] if a[i+1] <= n // 2 else n - a[i+1] + 1
		a[i] = a[i] if a[i] <= n // 2 else n - a[i] + 1
		if abs(left - a[i]) > 1 or abs(right - a[i]) > 1:
				flag = False
				break
	print("YES" if flag else "NO")


if __name__ == "__main__":
	for _ in range(int(input())):
		solve()
