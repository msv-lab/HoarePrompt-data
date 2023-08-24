def guaranteed_lead(n, points):
    # Get Julia's score
    julia_score = points[0]
    
    # Count the number of bettors with more points than Julia
    num_matches = sum(p > julia_score for p in points[1:])
    
    # Calculate the remaining matches
    remaining_matches = n - 1 - num_matches
    
    return remaining_matches

# Read input
n = int(input())
points = list(map(int, input().split()))

# Call function and print result
result = guaranteed_lead(n, points)
print(result)