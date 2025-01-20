s = input().strip()
dead_bulbs = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
positions = {}
for (i, char) in enumerate(s):
    if char in 'RBYG':
        positions[char] = i % 4
for (i, char) in enumerate(s):
    if char == '!':
        for (color, pos) in positions.items():
            if i % 4 == pos:
                dead_bulbs[color] += 1
print(dead_bulbs['R'], dead_bulbs['B'], dead_bulbs['Y'], dead_bulbs['G'])