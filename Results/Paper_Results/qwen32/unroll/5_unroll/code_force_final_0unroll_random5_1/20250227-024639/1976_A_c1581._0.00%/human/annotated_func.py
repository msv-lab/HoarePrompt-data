#State of the program right berfore the function call: password is a string consisting of exactly n characters, where each character is either a lowercase Latin letter or a digit, and n is an integer such that 1 ≤ n ≤ 20.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: `password` is a string consisting of exactly `n` characters, where each character is either a lowercase Latin letter or a digit, and `n` is an integer such that 1 ≤ n ≤ 20; `digits` is a list containing all the digit characters from the `password`; `letters` is a list containing all the lowercase Latin letter characters from the `password`.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: `last_digit_index` is the index of the last digit in `password` if there is at least one digit; otherwise, it is -1.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `last_digit_index` is the index of the last digit in `password` if there is at least one digit; otherwise, it is -1. The list `digits` is sorted.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `last_digit_index` is the index of the last digit in `password` if there is at least one digit; otherwise, it is -1. The list `digits` is sorted. The list `letters` is sorted.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` checks if the input `password` string meets specific criteria: all digits must appear before any letters, and both digits and letters must be in non-decreasing order. If the password meets these criteria, the function returns 'YES'; otherwise, it returns 'NO'.

