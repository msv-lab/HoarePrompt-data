def sum_average(n):
    # Calculate the sum using the formula for the sum of the first n natural numbers
    total_sum = n * (n + 1) // 2
    
    # Calculate the average
    average = total_sum / n
    
    # Return the result as a tuple
    return (total_sum, average)

# Test cases
assert sum_average(10) == (55, 5.5)
assert sum_average(15) == (120, 8.0)
assert sum_average(20) == (210, 10.5)
