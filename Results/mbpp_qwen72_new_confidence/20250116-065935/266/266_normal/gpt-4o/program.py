def bell_Number(n):
    # Create a table to store Bell numbers
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    
    # Base case: The 0th Bell number is 1
    bell[0][0] = 1
    
    # Fill the Bell table
    for i in range(1, n+1):
        # Explicitly put the Bell number of previous row at the first position of current row
        bell[i][0] = bell[i-1][i-1]
        
        # Fill the rest of the entries in the current row
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    
    # The nth Bell number is the first entry in the nth row
    return bell[n][0]

# Test cases
assert bell_Number(2) == 2
assert bell_Number(3) == 5
assert bell_Number(4) == 15
