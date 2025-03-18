#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, and `frequency` is a dictionary where each key is a digit from `digit_str` and its corresponding value is the count of occurrences of that digit in `digit_str`. If `n` is 0, then `digit_str` is "0" and `frequency` would be `{'0': 1}`.
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, `frequency` is a dictionary where for every digit, the count of occurrences of that digit is less than or equal to its integer value. If all conditions are satisfied, the function completes without returning False.
    return True
    #The program returns True, indicating that all conditions regarding the digit frequencies in the string representation of the non-negative integer 'n' are satisfied.
#Overall this is what the function does:The function accepts a non-negative integer `n`, counts the frequency of each digit in its string representation, and returns True if the count of each digit is less than or equal to the digit's value; otherwise, it returns False. If `n` contains any digit that appears more times than its value, the function will return False.

