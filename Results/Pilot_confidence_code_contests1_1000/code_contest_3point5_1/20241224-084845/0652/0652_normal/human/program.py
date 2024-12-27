import sys

def solve(n, a):
  if n == 1:
    print(0)
    return
  l = len(a)
  a.sort()
  least = -1
  for shift in range(0, l):
    curr = sub_solve(a, shift)
    if least == -1 or least > curr:
      least = curr
  print(least)

def sub_solve(a, s):
  l = len(a)
  min_x = a[s % l]
  max_x = a[(l/2 - 1 + s) % l]
  min_y = a[(l/2 + s) % l]
  max_y = a[(l-1 + s) % l]
  return abs(max_x - min_x) * abs(max_y - min_y)

n = sys.stdin.readline()
n = int(n)

ar = sys.stdin.readline()
ar = ar.split()
ar = [int(a) for a in ar if a and len(a) > 0]

solve(n, ar)
