# Educational Code Forces Round 87: C2: Not So Simple Polygon Embedding.
# Sun. May. 17, 2020, By: arccosh.

import math

def solve(n):
  return math.cos(math.pi / (4 * n)) / math.sin(math.pi / (2 * n))

for ca in xrange(int(raw_input())):
  n = int(raw_input())
  print('%.9f' % solve(n))
