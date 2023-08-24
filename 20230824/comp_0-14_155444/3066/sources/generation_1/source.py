def create_instructions(n, colors):
    instructions = []
    color_count = {}
    for i in range(n):
        color = colors[i]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    for color, count in color_count.items():
        if count > 1:
            return "IMPOSSIBLE"
    current_color = 0
    current_start = 1
    for i in range(n):
        color = colors[i]
        if color != current_color:
            if current_color != 0:
                instructions.append((current_start, i, current_color))
            current_color = color
            current_start = i + 1
    instructions.append((current_start, n, current_color))
    return instructions

n = int(input())
colors = list(map(int, input().split()))

instructions = create_instructions(n, colors)

if instructions == "IMPOSSIBLE":
    print("IMPOSSIBLE")
else:
    print(len(instructions))
    for instruction in instructions:
        print(instruction[0], instruction[1], instruction[2])