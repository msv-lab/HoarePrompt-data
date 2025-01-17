def min_jumps_to_home(n, d, s):
    # Initialize the jumps count and the current position
    jumps = 0
    position = 0

    # While the frog hasn't reached the last position
    while position < n - 1:
        # Find the farthest position the frog can jump to within the range [position + 1, position + d]
        next_position = position
        for i in range(position + 1, min(position + d + 1, n)):
            if s[i] == '1':
                next_position = i
        # If the frog cannot move forward, return -1
        if next_position == position:
            return -1
        # Move to the next position and increment the jump count
        position = next_position
        jumps += 1

    return jumps

# Read input
n, d = map(int, input().split())
s = input()

# Print the result
print(min_jumps_to_home(n, d, s))
