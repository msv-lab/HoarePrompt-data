#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, and `frequency` is a dictionary where each key is a unique digit from `digit_str` and its corresponding value is the frequency of that digit in `digit_str`.
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, `frequency` is a dictionary where each key is a unique digit from `digit_str` and its corresponding value is the frequency of that digit in `digit_str`, and for every key-value pair in `frequency`, the value (frequency) is less than or equal to the integer value of the key (digit).
    return True
    #The program returns True
#Overall this is what the function does:The function accepts a non-negative integer n, calculates the frequency of each digit in n, and returns True if the frequency of each digit is less than or equal to its integer value; otherwise, it returns False, with potential undefined behavior for negative integers and non-integers

