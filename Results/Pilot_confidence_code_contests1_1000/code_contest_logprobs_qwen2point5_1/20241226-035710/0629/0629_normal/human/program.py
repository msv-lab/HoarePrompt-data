# ------------------------------------------------
# -- Codeforces #252 - Problem C (Points on Line)
# -- http://codeforces.com/contest/252/problem/C
# -- Author: James Lawson <mail@jameslawson.io>
# ------------------------------------------------
from sys import stdin
from bisect import bisect_left

# -- O(nlgn)
def main(xs, d):
  total = 0
  start, count = 0, 1
  for i in range(1, len(xs)):
    if abs(xs[i] - xs[start]) <= d:
      # -- xs[i] is less than d distance from "start"
      #    so add it to the set
      count += 1
    else:
      # -- xs[i] is more than d distance from "start"
      #    so break apart the set, removing elements that
      #    are too far away from xs[i]
      #    before breaking, we'll add C(count, 3) to the total
      #    where count is size of the set
      new_start = bisect_left(xs, xs[i] - d, start, i)
      overlap = (i - 1) - new_start + 1
      total += (count * (count - 1) * (count - 2)) / 6
      if overlap > 0:
        total -= (overlap * (overlap - 1) * (overlap - 2)) / 6
      start = new_start
      count = i - new_start + 1
  total += (count * (count - 1) * (count - 2)) / 6
  return total

if __name__ == "__main__":
  n, d = map(int, stdin.readline().strip('\n').split(' '))
  xs = map(int, stdin.readline().strip('\n').split(' '))
  result = main(xs, d)
  print(result)
