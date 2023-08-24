"""
The problem statement asks to find the maximum number of executives that can be rewarded with bananas in a fair and evil manner.
Each executive must receive at least one briefcase and the total number of bananas received by a more evil executive must be greater than or equal to the total number of bananas received by a less evil executive.

To solve this problem, we can follow these steps:
1. Read the number of briefcases, N, from input.
2. Read the number of bananas in each briefcase, bananas, from input.
3. Sort the array bananas in non-decreasing order.
4. Initialize a variable, execs, to 0 to keep track of the number of executives rewarded.
5. Iterate through the briefcases, starting from the least evil executive.
   - For each briefcase, check if the total number of bananas given to the current executive is greater than or equal to the total number of bananas given to the previous executive.
   - If it is, increment the execs variable by 1.
6. Print the value of execs as the maximum number of executives that can be rewarded.

Let's implement this solution in code:
"""

N = int(input())  # Read the number of briefcases
bananas = list(map(int, input().split()))  # Read the number of bananas in each briefcase

bananas.sort()  # Sort the array in non-decreasing order
execs = 0  # Initialize the variable to keep track of the number of executives rewarded

# Iterate through the briefcases, starting from the least evil executive
for i in range(N):
    # Check if the total number of bananas given to the current executive is greater than or equal to the previous executive
    if sum(bananas[:i+1]) >= sum(bananas[:i]):
        execs += 1  # Increment the execs variable by 1

print(execs)  # Print the maximum number of executives that can be rewarded