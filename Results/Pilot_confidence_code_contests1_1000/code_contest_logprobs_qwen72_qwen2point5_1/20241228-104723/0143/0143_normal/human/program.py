#!/usr/bin/python

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(" "))

r = 0

s = [0] * (n+10)
si = 0

for x in a:
	if si>=2 and s[si-2] >= s[si-1] and s[si-1] <= x:
		r += s[si-1]
		si -= 1
	s[si] = x
	si += 1

for i in range(1, si-1):
	r += min(s[i-1], s[i+1])

print(r)