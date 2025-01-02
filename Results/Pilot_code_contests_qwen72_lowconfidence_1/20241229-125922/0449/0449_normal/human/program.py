import sys
import math

nCircles = int(sys.stdin.readline())

if nCircles < 1:
    sys.stdout.write('0\n')
    sys.exit()

areas = []
input = sys.stdin.readline()
for radius in input.split(' '):
    areas.append(int(radius)*int(radius))

areas.sort()

totalArea = 0
for index, area in enumerate(areas):
    if index == 0:
        totalArea += area
    elif index % 2 == 0:
        totalArea += (areas[index] - areas[index-1])

totalArea *= math.pi
sys.stdout.write(str(totalArea)+'\n')
