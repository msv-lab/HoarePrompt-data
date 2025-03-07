#State of the program right berfore the function call: password is a string of length n (1 ≤ n ≤ 20) consisting only of lowercase Latin letters and digits.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: `password` is a string of length n (1 ≤ n ≤ 20) consisting only of lowercase Latin letters and digits. `digits` is a list containing all the digits from the `password` string in the order they appear. `letters` is a list containing all the lowercase Latin letters from the `password` string in the order they appear.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: `password` is a string of length n (1 ≤ n ≤ 20) consisting only of lowercase Latin letters and digits. `i` is n-1, `char` is the last character of `password`. If `char` is a digit, `last_digit_index` is set to n-1. If `char` is not a digit and `last_digit_index` is not -1, the program returns 'NO'. Otherwise, `last_digit_index` is the index of the last digit in `password` or -1 if no digit is found.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'.
    #State: `password` is a string of length n (1 ≤ n ≤ 20) consisting only of lowercase Latin letters and digits. `i` is n-1, `char` is the last character of `password`. If `char` is a digit, `last_digit_index` is set to n-1. If `char` is not a digit and `last_digit_index` is not -1, the program returns 'NO'. Otherwise, `last_digit_index` is the index of the last digit in `password` or -1 if no digit is found. Additionally, the list `digits` is sorted.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `password` is a string of length n (1 ≤ n ≤ 20) consisting only of lowercase Latin letters and digits. `i` is n-1, `char` is the last character of `password`. If `char` is a digit, `last_digit_index` is set to n-1. If `char` is not a digit and `last_digit_index` is not -1, the program returns 'NO'. Otherwise, `last_digit_index` is the index of the last digit in `password` or -1 if no digit is found. Additionally, the list `digits` is sorted. The list `letters` is sorted.
    return 'YES'
    #The program returns 'YES'.
#Overall this is what the function does:The function `func_1` accepts a string `password` of length n (1 ≤ n ≤ 20) consisting only of lowercase Latin letters and digits. It returns 'YES' if the following conditions are met: all digits in the password are in non-decreasing order, all letters in the password are in non-decreasing order, and no letter appears after a digit in the password. If any of these conditions are not met, the function returns 'NO'.

