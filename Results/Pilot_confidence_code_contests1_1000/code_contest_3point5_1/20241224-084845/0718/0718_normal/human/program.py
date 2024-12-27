import sys
from fractions import gcd

c, h1, h2, w1, w2 = (int (t) for t in sys.stdin.readline().split())
g = gcd (w1, w2)
c /= g
w1 /= g
w2 /= g

res = 0
if c <= 10 ** 5 * w1:
  for i in range (c/w1 + 1):
    if res < i * h1 + (c - i*w1) / w2 * h2:
      res = i * h1 + (c - i*w1) / w2 * h2
elif c <= 10 ** 5 * w2:
  for i in range (c/w2 + 1):
    if res < i * h2 + (c - i*w2) / w1 * h1:
      res = i * h2 + (c - i*w2) / w1 * h1
else:
  if h1 * w2 < h2 * w1:
    h1, h2 = h2, h1
    w1, w2 = w2, w1
  for i in range (10 ** 5):
    if res < i * h2 + (c - i*w2) / w1 * h1:
      res = i * h2 + (c - i*w2) / w1 * h1

print (res)

    