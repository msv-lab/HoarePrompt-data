def min_slices_to_uniform_height(n, k, heights):
    heights.sort(reverse=True)
    slices = 0
    current_total_removed = 0
    current_height = heights[0]
    
    for i in range(n):
        if i > 0 and heights[i] != current_height:
            current_height = heights[i - 1]
            removed_per_tower = current_height - heights[i]
            total_removed = removed_per_tower * i
            
            if current_total_removed + total_removed > k:
                slices += 1
                current_total_removed = 0
            current_total_removed += total_removed
        
        current_height = heights[i]
    
    if current_total_removed > 0:
        slices += 1
    
    return slices

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
heights = list(map(int, data[2:]))

# Get result and print it
result = min_slices_to_uniform_height(n, k, heights)
print(result)
