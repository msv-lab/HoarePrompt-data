import sys
import math

# Read the input
r = int(sys.stdin.readline().strip())

# Calculate the area of the circle with radius r
area_r = math.pi * r**2

# Calculate the area of the circle with radius 1
area_1 = math.pi * 1**2

# Calculate the integer ratio (rounded down) of the two areas
ratio = int(area_r // area_1)

# Print the ratio
print(ratio)