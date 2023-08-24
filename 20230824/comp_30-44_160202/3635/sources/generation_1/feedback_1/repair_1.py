N = int(input())  # Read the number of briefcases
bananas = list(map(int, input().split()))  # Read the number of bananas in each briefcase

bananas.sort()  # Sort the array in non-decreasing order
execs = 0  # Initialize the variable to keep track of the number of executives rewarded

# Iterate through the briefcases, starting from the least evil executive
for i in range(1, N+1):
    # Check if the total number of bananas given to the current executive is greater than or equal to the previous executive
    if sum(bananas[:i+1]) >= sum(bananas[:i]) * (i+1)/i:
        execs += 1  # Increment the execs variable by 1 if it is less than i+1

print(execs)  # Print the maximum number of executives that can be rewarded