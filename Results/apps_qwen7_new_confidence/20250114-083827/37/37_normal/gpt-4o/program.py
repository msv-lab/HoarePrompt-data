def find_coordinates(n):
    # Directions in hexagonal grid
    directions = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
    
    x, y = 0, 0  # Starting position
    steps = 1    # Initial number of steps to take in a given direction
    direction_index = 0  # Start with the first direction
    
    while n > 0:
        for _ in range(2):  # Each direction length is repeated twice before increasing the steps
            if n >= steps:
                dx, dy = directions[direction_index]
                x += dx * steps
                y += dy * steps
                n -= steps
                direction_index = (direction_index + 1) % 6
            else:
                dx, dy = directions[direction_index]
                x += dx * n
                y += dy * n
                return x, y
        steps += 1  # Increase the number of steps after completing two directions
    
    return x, y

# Read input
n = int(input().strip())

# Get the coordinates after n moves
x, y = find_coordinates(n)

# Print the result
print(x, y)
