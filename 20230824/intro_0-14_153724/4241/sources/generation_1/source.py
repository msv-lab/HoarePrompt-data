def substring_changes(S, T):
    # Initialize the minimum_changes variable to keep track of the minimum number of changes needed
    minimum_changes = float('inf')

    # Iterate through each possible starting index in S
    for i in range(len(S) - len(T) + 1):
        changes = 0
        
        # Check if T is a substring of S starting from the current index
        for j in range(len(T)):
            if S[i+j] != T[j]:
                changes += 1
        
        # Update the minimum_changes if the current number of changes is smaller
        minimum_changes = min(minimum_changes, changes)

    return minimum_changes

# Read input S and T
S = input()
T = input()

# Call the substring_changes function and print the result
print(substring_changes(S, T))