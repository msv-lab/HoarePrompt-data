def count_full_glasses(n, t):
    # Initialize a 2D list to represent the glasses in the pyramid
    glasses = [[0] * (i + 1) for i in range(n)]
    
    # Pour champagne into the top glass
    glasses[0][0] = t
    
    # Distribute the champagne
    for i in range(n):
        for j in range(i + 1):
            if glasses[i][j] > 1:
                overflow = glasses[i][j] - 1
                glasses[i][j] = 1
                if i + 1 < n:
                    glasses[i + 1][j] += overflow / 2
                    glasses[i + 1][j + 1] += overflow / 2
    
    # Count the number of completely full glasses
    full_glasses_count = sum(glasses[i][j] == 1 for i in range(n) for j in range(i + 1))
    
    return full_glasses_count

# Read input
n, t = map(int, input().split())

# Get the number of full glasses
result = count_full_glasses(n, t)

# Print the result
print(result)
