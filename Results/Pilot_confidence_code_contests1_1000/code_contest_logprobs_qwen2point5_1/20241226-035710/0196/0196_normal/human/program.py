import sys

line_one = sys.stdin.readline().split()
line_two = sys.stdin.readline().split()

types = int(line_one[0])
pocket_limit = int(line_one[1])

pebbles = map(int, line_two)

days = 0
remaining_pebbles = sum(pebbles)

while remaining_pebbles > 0:
  days += 1
  pebbles = [pebble for pebble in pebbles if pebble > 0]
  pebbles.sort()
  if len(pebbles) > 1:
    pebbles[0] -= pocket_limit
    pebbles[1] -= pocket_limit
  elif len(pebbles) > 0:
    pebbles[0] -= 2 * pocket_limit
  remaining_pebbles = sum(pebbles)

print(days)
