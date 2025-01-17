def big_sum(arr):
    if not arr:
        return 0
    smallest = min(arr)
    largest = max(arr)
    return smallest + largest

# Test cases
assert big_sum([1, 2, 3]) == 4
assert big_sum([-1, 2, 3, 4]) == 3
assert big_sum([2, 3, 6]) == 8
