def turn_skewers(n, k):
    positions = []
    i = 1  # Start from the first skewer
    
    while i <= n:
        positions.append(i)
        i += 2 * k + 1  # Jump to the next segment that needs turning
    
    # Now print the results
    print(len(positions))
    print(" ".join(map(str, positions)))

# Read input
n, k = map(int, input().split())

# Execute function
turn_skewers(n, k)
