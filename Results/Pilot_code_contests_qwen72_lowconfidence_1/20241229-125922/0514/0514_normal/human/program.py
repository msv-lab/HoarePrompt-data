# -*- coding: utf-8 -*-

import sys

n, h = [int(e) for e in raw_input().split()]

kl = []
for i in range(0, n):
    a, b = [int(e) for e in raw_input().split()]
    kl.append((b, 0))
    kl.append((a, 1))

kl.sort(reverse=True)
# print kl

n = 0
i = 0
while h > 0:
    k = kl[i]
    if k[1] == 0:
        h -= k[0]
        i += 1
        n += 1
    else:
        n = n + ((h + k[0] - 1) / k[0])
        break

sys.stdout.write('%d\n' % (n))
sys.stdout.flush()
