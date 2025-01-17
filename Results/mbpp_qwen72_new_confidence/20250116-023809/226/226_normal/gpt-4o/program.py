def find_Odd_Pair(arr, n):
    odd_count = sum(1 for x in arr if x % 2 != 0)
    even_count = n - odd_count
    return odd_count * even_count

# Test cases
assert find_Odd_Pair([5,4,7,2,1],5) == 6
assert find_Odd_Pair([7,2,8,1,0,5,11],7) == 12
assert find_Odd_Pair([1,2,3],3) == 2
