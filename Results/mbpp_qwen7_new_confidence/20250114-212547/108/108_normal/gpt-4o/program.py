def get_total_number_of_sequences(m, n):
    # Memoization dictionary to store results of sub-problems
    memo = {}
    
    def count_sequences(last_num, length):
        # If the length is zero, there is one valid sequence (the empty sequence)
        if length == 0:
            return 1
        
        # Check if result is already computed
        if (last_num, length) in memo:
            return memo[(last_num, length)]
        
        # Initialize count
        count = 0
        
        # Loop through possible next elements
        for next_num in range(last_num * 2, m + 1):
            count += count_sequences(next_num, length - 1)
        
        # Memoize the result
        memo[(last_num, length)] = count
        return count
    
    # Total sequences starting from each possible first element
    total_count = 0
    for first_num in range(1, m + 1):
        total_count += count_sequences(first_num, n - 1)
    
    return total_count

# Tests
assert get_total_number_of_sequences(10, 4) == 4
assert get_total_number_of_sequences(5, 2) == 6
assert get_total_number_of_sequences(16, 3) == 84
