def armstrong_number(n):
    # Convert the number to string to easily iterate through its digits
    num_str = str(n)
    # Calculate the number of digits
    num_len = len(num_str)
    # Calculate the sum of the digits each raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    # Compare the sum to the original number
    return armstrong_sum == n

# Tests
assert armstrong_number(153) == True
assert armstrong_number(259) == False
assert armstrong_number(4458) == False
