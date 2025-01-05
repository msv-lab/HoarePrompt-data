# -*- coding: utf-8 -*-

import re

n = int(raw_input())
a = map(int, re.split("\s", raw_input()))
left = 0
right = 0
mask = 10**9 + 7

pow = [0]*n+2

tmp = 1
for i in range(1, n+2):
        tmp *= i
        pow[i] = tmp

for i in range(0, n + 1):
        x = a.index(a[i])
        if a[i] in a[x+1:]:
                left = i
                right = a[x+1:].index(a[i]) + x + 1
                break

for i in range(1, n + 2):
        ans = (pow[n + 1] / (pow[i] * pow[n + 1 - i]))
        x = (pow[left + n - right] / (pow[i - 1] * pow[left + n - right - i + 1]))
        print (ans - x) % mask