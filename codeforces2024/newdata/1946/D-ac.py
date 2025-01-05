def func(n, x, a):
    val = 0  # This will store the cumulative XOR for the current segment
    ct = 0   # This counts the number of valid segments
    for z in a:
        z = int(z)  # Ensure the element is an integer
        val ^= z    # Update the cumulative XOR with the current element
        # Check if the current segment can be closed
        if val | x == x:
            ct += 1  # Increment the segment count
            val = 0  # Reset the cumulative XOR for the next segment
    # If val is 0, all segments are valid, return the count
    if val == 0:
        return ct
    else:
        return -1  # Otherwise, return -1 indicating no valid segmentation

t = int(input())  # Read the number of test cases
for _ in range(t):
    n, x = [int(z) for z in input().split()]  # Read n and x for the test case
    a = [int(z) for z in input().split()]     # Read the array a
    best = -1  # Initialize the best result for this test case
    highbit = 1  # This will help in manipulating x
    while highbit:
        # Try to find the maximum k for the current x
        best = max(best, func(n, x + highbit - 1, a))
        highbit = x & -x  # Get the lowest set bit in x
        x ^= highbit      # Remove the lowest set bit from x
    print(best)  # Output the best result for the current test case