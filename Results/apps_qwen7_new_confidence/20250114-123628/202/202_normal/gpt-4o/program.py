def max_joy(C, H_r, H_b, W_r, W_b):
    max_joy_units = 0

    # Try to maximize joy by iterating over number of red candies
    for red_candies in range(0, C // W_r + 1):
        remaining_capacity = C - red_candies * W_r
        blue_candies = remaining_capacity // W_b
        joy_units = red_candies * H_r + blue_candies * H_b
        max_joy_units = max(max_joy_units, joy_units)

    return max_joy_units

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
C, H_r, H_b, W_r, W_b = map(int, data)

# Print the maximum number of joy units
print(max_joy(C, H_r, H_b, W_r, W_b))
