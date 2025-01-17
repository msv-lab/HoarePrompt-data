def square_Sum(n):
    total_sum = 0
    odd_number = 1
    for _ in range(n):
        total_sum += odd_number ** 2
        odd_number += 2
    return total_sum

# Testing the function with provided test cases
assert square_Sum(2) == 10
assert square_Sum(3) == 35
assert square_Sum(4) == 84
