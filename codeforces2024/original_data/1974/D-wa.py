def distribute_instructions(n, s):
    count_north = 0
    count_south = 0
    count_east = 0
    count_west = 0

    # Count occurrences of each direction
    for char in s:
        if char == 'N':
            count_north += 1
        elif char == 'S':
            count_south += 1
        elif char == 'E':
            count_east += 1
        else:  # char == 'W'
            count_west += 1

    # Determine if it's possible to balance the movements
    if count_north != count_south or count_east != count_west:
        return "NO"

    result = []

    # Distribute instructions
    i = 0
    while i < len(s):
        if s[i] == 'N' or s[i] == 'S':
            if s[i] == 'N':
                result.append('R')
                count_north -= 1
            else:
                result.append('H')
                count_south -= 1
            i += 1
        elif s[i] == 'E' or s[i] == 'W':
            if s[i] == 'E':
                result.append('R')
                count_east -= 1
            else:
                result.append('H')
                count_west -= 1
            i += 1

    return ''.join(result)

# Read input
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    s = data[index]
    index += 1
    results.append(distribute_instructions(n, s))

# Print results
print('\n'.join(results))