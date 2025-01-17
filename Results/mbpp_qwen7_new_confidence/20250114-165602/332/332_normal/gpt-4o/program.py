def odd_num_sum(n: int) -> int:
    # Generate the first n odd natural numbers
    odd_numbers = [i for i in range(1, 2*n, 2)]
    
    # Compute the fourth power of each odd number and sum them up
    result = sum([num**4 for num in odd_numbers])
    
    return result

# Test cases
assert odd_num_sum(2) == 82
assert odd_num_sum(3) == 707
assert odd_num_sum(4) == 3108
