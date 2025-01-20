def find_even_pair(lst):
    even_count = sum(1 for x in lst if x % 2 == 0)
    odd_count = len(lst) - even_count  # total count minus even count gives odd count

    # Calculate the number of pairs that XOR to an even number
    even_pairs = even_count * (even_count - 1) // 2
    odd_pairs = odd_count * (odd_count - 1) // 2
    
    return even_pairs + odd_pairs

# Test cases
assert find_even_pair([5, 4, 7, 2, 1]) == 4
assert find_even_pair([7, 2, 8, 1, 0, 5, 11]) == 9
assert find_even_pair([1, 2, 3]) == 1
