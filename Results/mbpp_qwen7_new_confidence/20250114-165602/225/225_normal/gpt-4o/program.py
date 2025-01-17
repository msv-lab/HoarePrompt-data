def difference(n):
    # Calculate the sum of the first n natural numbers
    sum_n = n * (n + 1) // 2
    
    # Calculate the sum of the cubes of the first n natural numbers
    sum_cubes_n = sum_n ** 2
    
    # Calculate the difference
    return sum_cubes_n - sum_n

# Tests
assert difference(3) == 30
assert difference(5) == 210
assert difference(2) == 6
