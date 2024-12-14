import math

def min_segments(n):
    min_segments_needed = float('inf')
    
    for a in range(1, int(math.sqrt(n)) + 1):
        b = (n + a - 1) // a  # This is equivalent to math.ceil(n / a)
        segments_needed = 2 * (a + b)
        min_segments_needed = min(min_segments_needed, segments_needed)
    
    return min_segments_needed

# Read input
n = int(input().strip())

# Output the result
print(min_segments(n))
