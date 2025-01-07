#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, `frequency` is a dictionary that contains the count of each digit present in `digit_str`. If `n` is 0, `digit_str` is "0", and `frequency` is {'0': 1}. If `n` is greater than 0, `frequency` corresponds to the counts of each digit in the string representation of `n`.
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, `frequency` contains the count of each digit in `digit_str`, and for every digit in `frequency`, the count is less than or equal to the integer value of that digit.
    return True
    #The program returns True, indicating that the frequency of each digit in the string representation of the non-negative integer 'n' is less than or equal to the integer value of that digit.
#Overall this is what the function does:The function accepts a non-negative integer `n`, calculates the frequency of each digit in its string representation, and returns True if the frequency of each digit is less than or equal to the integer value of that digit; otherwise, it returns False. It does not account for negative integers or non-integer types, as the input is assumed to be a non-negative integer.

