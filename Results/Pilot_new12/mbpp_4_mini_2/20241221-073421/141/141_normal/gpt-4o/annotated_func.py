#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is a string representation of `n`, and `frequency` is a dictionary where each key represents a digit in `digit_str`, and its value represents the count of how many times that digit appears in `digit_str`.
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, `frequency` is a dictionary where the count of each digit in `digit_str` is less than or equal to the integer value of that digit.
    return True
    #The program returns True, indicating that the count of each digit in the string representation of n does not exceed the integer value of that digit.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and verifies whether the count of each digit in the string representation of `n` does not exceed the integer value of that digit. It constructs a frequency dictionary that counts how many times each digit appears. The function will return `False` if any digit's count exceeds its value, otherwise it returns `True`. If `n` is zero, the function will correctly handle this case since the digit '0' appears once and meets the condition of the check. The function does not handle negative integers, as stated in the precondition, and it is limited to non-negative integers only.

