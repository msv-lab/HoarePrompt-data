x = int(input())
normalized_angle = x % 360
turns = (360 - normalized_angle) // 90 % 4
print(turns)