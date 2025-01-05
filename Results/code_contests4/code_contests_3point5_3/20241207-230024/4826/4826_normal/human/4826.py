import sys

cities = int(sys.stdin.readline())
coordinates = map(int, sys.stdin.readline().split())
coordinates.sort()

dist = 2*10**9
count = 0
for index, x in enumerate(coordinates):
  if index < len(coordinates) - 1:
    temp_dist = coordinates[index + 1] - x
    if temp_dist < dist:
      dist = temp_dist
      count = 1
    elif temp_dist == dist:
      count += 1

print(str(dist) + ' ' + str(count))
