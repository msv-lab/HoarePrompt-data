def guaranteed_lead(n, points):
    max_points = max(points)
    num_matches = 0
    
    for p in points[1:]:
        if p == max_points:
            num_matches += 1
    
    return num_matches

# Read input
n = int(input())
points = list(map(int, input().split()))

# Call function and print result
result = guaranteed_lead(n, points)
print(result)