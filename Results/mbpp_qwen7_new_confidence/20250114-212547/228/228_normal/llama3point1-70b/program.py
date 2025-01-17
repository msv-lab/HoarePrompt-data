def digit_distance_nums(num1: int, num2: int) -> int:
    """
    Calculate the sum of the per-digit difference between two integers.
    
    Args:
    num1 (int): The first integer.
    num2 (int): The second integer.
    
    Returns:
    int: The sum of the per-digit difference between num1 and num2.
    """
    # Convert the integers to strings to easily access each digit
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Initialize the sum of differences
    sum_diff = 0
    
    # Iterate over the digits of the numbers
    for digit1, digit2 in zip(str_num1, str_num2):
        # Calculate the absolute difference between the digits
        diff = abs(int(digit1) - int(digit2))
        # Add the difference to the sum
        sum_diff += diff
    
    # If one number has more digits than the other, add the remaining digits to the sum
    if len(str_num1) > len(str_num2):
        for digit in str_num1[len(str_num2):]:
            sum_diff += int(digit)
    elif len(str_num2) > len(str_num1):
        for digit in str_num2[len(str_num1):]:
            sum_diff += int(digit)
    
    return sum_diff
