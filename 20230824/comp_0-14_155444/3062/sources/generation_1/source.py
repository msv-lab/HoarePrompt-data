import math

x, y = map(int, input().split())
v, w = map(float, input().split())

# calculate the Euclidean distance
distance = math.sqrt(x**2 + y**2)

# calculate the time to travel straight
straight_time = distance / v

# calculate the angle to turn
angle = math.atan2(y, x)

# calculate the time to rotate
rotate_time = angle / w

# calculate the total time
total_time = straight_time + rotate_time

# print the result with 8 decimal places
print("{:.8f}".format(total_time))