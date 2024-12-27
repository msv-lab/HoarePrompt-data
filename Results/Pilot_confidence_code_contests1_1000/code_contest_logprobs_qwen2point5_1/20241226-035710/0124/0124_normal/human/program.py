from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

rectangle = diamond = 0
for line in stdin:
    try:
        a, b, c = (int(s) for s in line.split(','))
    except ValueError:
        break
    diamond += a == b
    rectangle += a ** 2 + b ** 2 == c ** 2
print(rectangle, diamond, sep='\n')