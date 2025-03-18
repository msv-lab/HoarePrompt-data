#State of the program right berfore the function call: password is a string consisting of lowercase Latin letters and digits, with a length between 1 and 20 inclusive.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: `password` is a string consisting of lowercase Latin letters and digits, with a length between 1 and 20 inclusive. `digits` is a list containing all the digits from `password` in the order they appear. `letters` is a list containing all the lowercase Latin letters from `password` in the order they appear.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: After the loop executes all iterations, `password` remains a string consisting of lowercase Latin letters and digits, with a length between 1 and 20 inclusive. If `password` contains at least one digit and no lowercase Latin letter immediately follows a digit, `last_digit_index` is the index of the last digit in `password`. If `password` contains a lowercase Latin letter immediately following a digit, the loop returns 'NO' and the program terminates. If `password` contains no digits, `last_digit_index` remains -1.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: After the loop executes all iterations, `password` remains a string consisting of lowercase Latin letters and digits, with a length between 1 and 20 inclusive. If `password` contains at least one digit and no lowercase Latin letter immediately follows a digit, `last_digit_index` is the index of the last digit in `password`. If `password` contains a lowercase Latin letter immediately following a digit, the loop returns 'NO' and the program terminates. If `password` contains no digits, `last_digit_index` remains -1. Additionally, the digits in `password` are in sorted order.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `password` remains a string consisting of lowercase Latin letters and digits, with a length between 1 and 20 inclusive. If `password` contains at least one digit and no lowercase Latin letter immediately follows a digit, `last_digit_index` is the index of the last digit in `password`. If `password` contains a lowercase Latin letter immediately following a digit, the loop returns 'NO' and the program terminates. If `password` contains no digits, `last_digit_index` remains -1. Additionally, the digits in `password` are in sorted order, and the lowercase Latin letters in `password` are in sorted order.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts a string `password` consisting of lowercase Latin letters and digits, with a length between 1 and 20 inclusive. It returns 'YES' if the password meets the following criteria: all digits in the password are in sorted order, all lowercase Latin letters in the password are in sorted order, and no lowercase Latin letter immediately follows a digit. If any of these criteria are not met, the function returns 'NO'.

