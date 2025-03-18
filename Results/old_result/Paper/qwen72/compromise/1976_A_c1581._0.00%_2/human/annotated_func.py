#State of the program right berfore the function call: password is a string consisting of lowercase Latin letters and digits, with a length between 1 and 20 inclusive.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: digits is a list containing all the digits from the string password in the order they appear; letters is a list containing all the lowercase Latin letters from the string password in the order they appear.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: `digits` is a list containing all the digits from the string `password` in the order they appear; `letters` is a list containing all the lowercase Latin letters from the string `password` in the order they appear; `last_digit_index` is the index of the last digit in `password` or -1 if there are no digits.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: *`digits` is a list containing all the digits from the string `password` in the order they appear; `letters` is a list containing all the lowercase Latin letters from the string `password` in the order they appear; `last_digit_index` is the index of the last digit in `password` or -1 if there are no digits. Additionally, `digits` is sorted in non-decreasing order.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `digits` is a list containing all the digits from the string `password` in the order they appear; `letters` is a list containing all the lowercase Latin letters from the string `password` in the order they appear; `last_digit_index` is the index of the last digit in `password` or -1 if there are no digits. Additionally, `digits` is sorted in non-decreasing order, and `letters` is sorted in non-decreasing order.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` takes a string `password` consisting of lowercase Latin letters and digits, with a length between 1 and 20 inclusive. It returns 'NO' if the digits in the password are not in non-decreasing order, or if any letter appears after a digit and before another digit. It returns 'YES' if the digits are in non-decreasing order and all letters appear either before or after all digits.

