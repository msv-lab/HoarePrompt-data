#!/usr/bin/env python
# -*- coding: utf-8 -*-

N = input()
S = raw_input.split()
for i in range(N):
	if S[i] == 'Y':
		print('Four')
		N = -1
		break
if N == -1:
	print('Three')