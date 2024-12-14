x = int(input())

# Normalize the angle to be within the range of 0 to 360 degrees
normalized_angle = x % 360

# Calculate the minimum number of 90 degrees clockwise turns needed
# to make the image as close to vertical as possible
turns = (360 - normalized_angle) // 90 % 4

print(turns)
