#!/usr/bin/env python
# -*- coding: utf-8 -*-

a, b, c = map(int, raw_input().split())
for i in range(10000):
	if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
		print(i)
		quit()
	a, b, c = b / 2 + c / 2, a / 2 + c / 2, a / 2 + b / 2
print(-1) 