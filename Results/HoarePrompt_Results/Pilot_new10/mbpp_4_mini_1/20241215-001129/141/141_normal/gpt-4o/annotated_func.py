#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
        
    #State of the program after the  for loop has been executed: `frequency` is a dictionary mapping each digit in the string representation of `n` to its frequency, `digit_str` is the string representation of `n`, and `n` is a non-negative integer.
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `frequency` is a dictionary with counts for each digit in `digit_str`, `digit_str` is the string representation of `n`, `n` is a non-negative integer, and for every digit in `frequency`, its count is less than or equal to the integer value of that digit.
    return True
    #The program returns True, indicating that for every digit in the frequency dictionary, its count is less than or equal to the integer value of that digit.
#Overall this is what the function does:The function accepts a non-negative integer `n` and checks the frequency of each digit in `n`. It returns `False` if the count of any digit exceeds its integer value. If all digit counts are less than or equal to their respective digit values, it returns `True`. The function doesn't handle invalid inputs (like negative numbers) explicitly, though the function is intended for non-negative integers according to the initial condition.

