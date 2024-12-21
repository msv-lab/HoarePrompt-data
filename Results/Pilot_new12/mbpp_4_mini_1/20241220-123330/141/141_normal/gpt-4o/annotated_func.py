#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is a string representation of `n`, `frequency` is a dictionary where each key is a digit present in `digit_str`, and the corresponding value is the count of how many times that digit appears in `digit_str`. If `n` is 0, then `digit_str` is "0", and `frequency` is `{"0": 1}`.
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, `frequency` is a dictionary where each digit key in `frequency` has a corresponding count value that is less than or equal to the integer value of that digit. If `n` is 0, `digit_str` is "0", and `frequency` is `{"0": 1}`.
    return True
    #The program returns True.
#Overall this is what the function does:Functionality: The function `func_1` accepts a non-negative integer `n` and determines if the count of each digit in its string representation (`digit_str`) does not exceed the integer value of that digit. It constructs a frequency dictionary to keep track of how many times each digit appears. If any digit has a count greater than its integer value, the function returns `False`. If all digits satisfy the condition, the function returns `True`. Notably, the function specifically handles the case when `n` is 0, resulting in a frequency dictionary of `{"0": 1}`, which returns `False` as 1 is greater than the integer value of 0. The final state of the program indicates whether or not the digit count constraints were upheld.

