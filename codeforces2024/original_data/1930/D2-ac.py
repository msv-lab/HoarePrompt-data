def res(n, m):
    # Prepend a '?' to the string to make it 1-indexed for easier handling
    s = "?" + m
    # Initialize an array to store the contribution of each position
    l = [0] * (n + 1)
    # Variable to store the final result
    out = 0
    
    # Iterate from the end of the string to the beginning
    for i in range(n, 0, -1):
        if s[i] == '1':
            # If the current character is '1', calculate its contribution
            if i + 3 <= n:
                # If there is room for a substring of length 3 starting at i
                l[i] = n + 1 - i + l[i + 3]
            else:
                # Otherwise, just consider the remaining length
                l[i] = n + 1 - i
        else:
            # If the current character is '0', carry forward the contribution
            if i + 1 <= n:
                l[i] = l[i + 1]
            else:
                l[i] = 0
        
        # Add the contribution of the current position to the result
        out += l[i]
    
    # Print the result for the current test case
    print(out)

# Read the number of test cases
t = int(input())
for _ in range(t):
    # Read the length of the binary string
    n = int(input())
    # Read the binary string
    t1 = input()
    # Calculate and print the result for the current test case
    res(n, t1)