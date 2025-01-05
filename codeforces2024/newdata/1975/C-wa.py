from collections import Counter

def max_possible_value(arr):
    counter = Counter(arr)
    left, right = min(counter.keys()), max(counter.keys())
    
    while left < right:
        mid = (left + right + 1) // 2
        count = sum(val for key, val in counter.items() if key >= mid)
        
        if count * (mid - 1) <= len(arr):
            left = mid
        else:
            right = mid - 1
            
    return left

# Test the function
print(max_possible_value([1, 2, 3, 4, 5])) # Output: 4
print(max_possible_value([1, 2, 1, 2, 1])) # Output: 1