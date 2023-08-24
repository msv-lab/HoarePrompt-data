from typing import List

def reorder_array(n: int, arr: List[int]) -> List[int]:
    # Compare the sums of the first n elements and the last n elements
    if sum(arr[:n]) == sum(arr[n:]):
        return [-1]
    
    return arr

# Read the input values
n = int(input())
arr = list(map(int, input().split()))

# Reorder the array
reordered_array = reorder_array(n, arr)

# Output the result
print(' '.join(map(str, reordered_array)))