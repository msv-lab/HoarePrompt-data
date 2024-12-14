def min_subsegment_length_to_target(n, operations, x, y):
    # Initial final position after following all operations
    final_x = 0
    final_y = 0

    # Compute the final coordinates after performing all operations
    for op in operations:
        if op == 'U':
            final_y += 1
        elif op == 'D':
            final_y -= 1
        elif op == 'L':
            final_x -= 1
        elif op == 'R':
            final_x += 1

    # The difference we need to correct
    dx = x - final_x
    dy = y - final_y

    # If the difference is already zero, no changes are needed
    if dx == 0 and dy == 0:
        return 0

    # Sliding window to determine the minimum subsegment length
    min_length = float('inf')
    current_x = 0
    current_y = 0

    # Dictionary to store the position of the robot at each step
    position_map = {(0, 0): -1}
    
    for i in range(n):
        if operations[i] == 'U':
            current_y += 1
        elif operations[i] == 'D':
            current_y -= 1
        elif operations[i] == 'L':
            current_x -= 1
        elif operations[i] == 'R':
            current_x += 1

        # If we have seen the position that would correct the difference before
        target_pos = (current_x + dx, current_y + dy)
        if target_pos in position_map:
            min_length = min(min_length, i - position_map[target_pos])

        position_map[(current_x, current_y)] = i

    return min_length if min_length != float('inf') else -1

# Read input
n = int(input())
operations = input().strip()
x, y = map(int, input().split())

# Get the result
result = min_subsegment_length_to_target(n, operations, x, y)
print(result)
