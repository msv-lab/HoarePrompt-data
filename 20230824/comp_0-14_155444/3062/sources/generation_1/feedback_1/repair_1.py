import math

x, y = map(int, input().split())
v, w = map(float, input().split())

# calculate the Euclidean distance
distance = math.sqrt(x**2 + y**2)

# calculate the angle to turn
angle = math.atan2(y, x)

# calculate the time to rotate
rotate_time = angle / w

# calculate the time to travel straight
if w == 0 or angle == 0:
    straight_time = distance / v
else:
    straight_time = abs(angle) / w + distance / v

# calculate the total time
total_time = straight_time + rotate_time

# print the result with 8 decimal places
print("{:.8f}".format(total_time))