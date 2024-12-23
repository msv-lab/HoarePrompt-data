#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    digit_str = str(n)
    frequency = {}
    for digit in digit_str:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, `frequency` is a dictionary where each key is a distinct digit from `digit_str`, and each corresponding value is the count of how many times that digit appears in `digit_str`. If `n` is 0, `digit_str` will be "0" and `frequency` will be {'0': 1}. If `n` is greater than 0, `frequency` will include digits present in the string representation of `n` with their respective counts.
    for (digit, count) in frequency.items():
        if count > int(digit):
            return False
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `digit_str` is the string representation of `n`, `frequency` is a dictionary where for every digit key, the value count of that key is less than or equal to the integer value of the digit. If `n` is 0, then frequency will be {'0': 1}. If `n` is greater than 0, then frequency contains all distinct digits of `n` with their respective counts satisfying the condition mentioned.
    return True
    #The program returns True, indicating that the frequency of each digit in the string representation of the non-negative integer n satisfies the defined condition
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and analyzes the frequency of each digit in its string representation. It constructs a dictionary `frequency` that counts how many times each digit appears. The function then checks whether the count of each digit is less than or equal to the digit's value. If any digit's count exceeds its numeric value, the function returns `False`. If all digit counts satisfy this condition, the function returns `True`. Edge cases include handling the input `0`, which is correctly represented, resulting in a frequency of `{'0': 1}`, and thus returning `False`, as `1` (frequency) is not less than or equal to `0` (value of digit). The function correctly handles any non-negative integer, including multi-digit numbers and those with repeating digits.

