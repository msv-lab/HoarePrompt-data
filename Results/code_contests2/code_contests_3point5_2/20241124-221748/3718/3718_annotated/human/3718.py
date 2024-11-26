from math import *

def distance(x1, y1, x2, y2):
  return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

x1, y1, r1 = map(int, raw_input().split())
x2, y2, r2 = map(int, raw_input().split())
d = distance(x1, y1, x2, y2)

r = 0.0
if r1 + r2 < d:
  r = (d - r1 - r2) / 2.0
elif abs(r1 - r2) > d:
  r = (abs(r1 - r2) - d) / 2.0
  
print("{:.6f}".format(r))