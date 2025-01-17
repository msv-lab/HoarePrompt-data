for _ in range(int(input())):
    n = int(input())
    
    # Determine whether to play first or second based on the number of 1s in the binary representation of n
    if bin(n).count('1') & 1:
        # If the count of 1s is odd, choose to play second
        print('second')
    else:
        # If the count of 1s is even, choose to play first
        print('first')
        
        # Calculate l by removing the first '1' from the binary representation of n
        l = int(bin(n)[3:], 2)
        
        # Print the two numbers p1 and p2 such that p1 XOR p2 = n
        print(n ^ l, l)
    
    # Continue the game until a break condition is met
    while True:
        a, b = map(int, input().split())
        
        # If both numbers are the same, it means the opponent cannot break further
        if a == b:
            break
        
        # Choose the number for the next round based on the number of 1s in its binary representation
        n = b if bin(a).count('1') & 1 else a
        
        # Calculate l for the chosen number
        l = int(bin(n)[3:], 2)
        
        # Print the two numbers for the next move
        print(n ^ l, l)