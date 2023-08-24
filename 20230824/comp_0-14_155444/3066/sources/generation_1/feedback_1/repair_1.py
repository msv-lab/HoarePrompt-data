
def create_instructions(n, colors):
    instructions = []
    color_count = {}
    
    # Count the number of instances of each color
    for i in range(n):
        color = colors[i]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    
    # Check if there are more color instances than the length of the plank
    for count in color_count.values():
        if count > n:
            return "IMPOSSIBLE"
    
    current_color = None
    current_start = 1
    
    # Create the instructions
    for i in range(1, n+1):
        color = colors[i-1]
        
        # If the color changes, add an instruction
        if color != current_color:
            if current_color is not None:
                instructions.append("{} {} {}".format(current_start, i-1, current_color))
            current_color = color
            current_start = i
    
    # Add the last instruction
    instructions.append("{} {} {}".format(current_start, n, current_color))
    
    return instructions


# Read the input
n = int(input())
colors = list(map(int, input().split()))

# Create the instructions
instructions = create_instructions(n, colors)

# Print the output
if instructions == "IMPOSSIBLE":
    print("IMPOSSIBLE")
else:
    print(len(instructions))
    for instruction in instructions:
        print(instruction)
