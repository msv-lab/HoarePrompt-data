for _ in range(int(input())):
    x = int(input())
    # Convert X to binary string
    s = bin(x)
    
    # Create a list of indices from 0 to the length of the binary string minus 3
    a = [*range(len(s[3:]))]
    
    # List to store positions of '1's in the binary representation
    b = []
    v = 0  # Position counter
    
    # Iterate over the binary string from the end to the third character
    for i in range(len(s) - 1, 2, -1):
        if s[i] == '1':
            # If the bit is '1', append the current position to b
            b.append(v)
        v += 1  # Increment position counter
    
    # Concatenate a and the reversed b to form the final answer
    ans = a + b[::-1]
    
    # Print the length of the array and the array itself
    print(len(ans))
    print(*ans)