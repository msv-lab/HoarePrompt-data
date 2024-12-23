#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is an empty string, and `frequency` is a dictionary containing the frequency of each digit in the original `digit_str`.
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `digit_str` is an empty string, `n` is a non-negative integer, and `frequency` is a dictionary where the count for every digit key is less than or equal to the integer value of the digit.
    return True
    #The program returns True
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` as input. It first converts `n` to a string and counts the frequency of each digit in `n`. After counting the frequencies, it checks each digit's frequency against the digit itself. If for any digit, its frequency is greater than the digit itself, the function returns `False`. Otherwise, it returns `True`. The function covers all possible cases for the input `n`, returning `False` if any digit's frequency exceeds the digit itself, and `True` only if no such digit exists.

