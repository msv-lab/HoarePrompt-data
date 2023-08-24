# Read inputs
n, t = map(int, input().split())

# Initialize the number of completely full glasses to 0
full_glasses = 0

# Iterate through each level of the pyramid
for level in range(1, n+1):
    # Calculate the number of glasses in the current level
    num_glasses = level
    
    # Calculate the total capacity of the glasses in the current level
    total_capacity = num_glasses ** 2
    
    # Calculate the amount of champagne poured into each glass per second
    champagne_per_glass = t / total_capacity
    
    # Check if the champagne overflows from the glasses in the current level
    if champagne_per_glass >= 1:
        # Update the number of completely full glasses with the number of glasses in the current level
        full_glasses += num_glasses
        # Reduce the remaining time by the time it takes to fill the glasses in the current level
        t -= total_capacity * champagne_per_glass
    
    # Otherwise, calculate the number of completely full glasses in the current level
    else:
        # Update the number of completely full glasses with the number of glasses in the current level multiplied by the amount of champagne poured into each glass per second
        full_glasses += int(champagne_per_glass * num_glasses)

# Print the number of completely full glasses
print(full_glasses)