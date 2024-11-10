def can_find_interval(n, m, colors, k):
    # We will create a sliding window to find the interval
    from collections import defaultdict
    
    # Desired counts for each color
    desired_counts = dict(zip(range(1, m+1), k))
    
    # Current counts in the sliding window
    current_counts = defaultdict(int)
    
    # Initialize two pointers for the sliding window
    left = 0
    
    for right in range(n):
        current_counts[colors[right]] += 1
        
        # Check if current window meets the condition
        while all(current_counts[color] >= desired_counts[color] for color in desired_counts):
            if all(current_counts[color] == desired_counts[color] for color in desired_counts):
                return "YES"
            current_counts[colors[left]] -= 1
            left += 1
    
    return "NO"

# Read input
n, m = map(int, input().split())
colors = list(map(int, input().split()))
k = list(map(int, input().split()))

# Output the result
print(can_find_interval(n, m, colors, k))
