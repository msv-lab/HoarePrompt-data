T = int(input())  # Number of test cases
for _ in range(T):
    n = int(input())  # Number of leaves
    stack = [[-1, 0]]  # Initialize stack with a dummy level
    top = 1  # Start with the first level
    win = "YES"  # Assume the tree can be constructed
    zct = 0  # Counter for leaves at distance 1 (root level)
    
    # Read the distances and process each leaf
    for x in input().split():
        x = int(x) + 1  # Convert distance to 1-based index
        zct += x == 1  # Count leaves at the root level
        
        # Check if the current distance is valid
        if x <= stack[-1][1]:
            win = "NO"  # Invalid if current distance is less than or equal to max nodes at last level
            break
        elif x == stack[-1][1] + 1:
            # If current distance is exactly one more than max nodes at last level
            if stack[-1][0] == stack[-1][1]:
                stack.pop()  # Remove the last level if fully utilized
            else:
                stack[-1][1] -= 1  # Decrement the count of nodes at last level
        elif top <= x - 2:
            # If current distance is greater than last level's max nodes by more than one
            stack.append([top, x - 2])  # Add a new level to the stack
        
        top = x  # Update the current level
    
    # Final check for valid tree structure
    if stack != [[-1, -1]] or zct != 1:
        win = "NO"  # Invalid if stack is not in expected state or no root level leaf
    
    print(win)  # Output the result for the test case