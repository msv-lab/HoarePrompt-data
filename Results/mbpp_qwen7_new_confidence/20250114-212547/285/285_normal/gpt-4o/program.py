import heapq

def heap_sort(nums):
    # Create a min heap from the list
    heapq.heapify(nums)
    
    # Extract elements from the heap in sorted order
    sorted_nums = [heapq.heappop(nums) for _ in range(len(nums))]
    
    return sorted_nums

# Tests
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert heap_sort([25, 35, 22, 85, 14, 65, 75, 25, 58]) == [14, 22, 25, 25, 35, 58, 65, 75, 85]
assert heap_sort([7, 1, 9, 5]) == [1, 5, 7, 9]
