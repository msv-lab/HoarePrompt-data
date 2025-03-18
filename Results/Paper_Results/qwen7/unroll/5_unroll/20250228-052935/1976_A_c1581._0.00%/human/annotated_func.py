#State of the program right berfore the function call: password is a string consisting of exactly n characters, where each character is either a lowercase Latin letter or a digit.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: Output State: `password` is a string consisting of exactly `n` characters, where each character is either a lowercase Latin letter or a digit; `digits` is a list containing all the digits from the original `password` string; `letters` is a list containing all the lowercase Latin letters from the original `password` string.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: Output State: `password` is a string consisting of exactly `n` characters, where each character is either a lowercase Latin letter or a digit; `digits` is a list containing all the digits from the original `password` string; `letters` is a list containing all the lowercase Latin letters from the original `password` string; `last_digit_index` is the index of the last digit in the `password` string if there is at least one digit, otherwise it remains -1. If the loop encounters a lowercase letter before any digit, it returns 'NO'.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `password` is a string consisting of exactly `n` characters, where each character is either a lowercase Latin letter or a digit; `digits` is a list containing all the digits from the original `password` string; `letters` is a list containing all the lowercase Latin letters from the original `password` string; `last_digit_index` is the index of the last digit in the `password` string if there is at least one digit, otherwise it remains -1; the `digits` list is sorted.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `password` is a string consisting of exactly `n` characters, where each character is either a lowercase Latin letter or a digit; `digits` is a list containing all the digits from the original `password` string; `letters` is a list containing all the lowercase Latin letters from the original `password` string; `last_digit_index` is the index of the last digit in the `password` string if there is at least one digit, otherwise it remains -1; the `digits` list is sorted; the `letters` list is sorted
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts a password string and checks if it meets specific conditions. It returns 'YES' if the password contains digits and letters that are both sorted in ascending order, and the last digit appears after all the letters. Otherwise, it returns 'NO'.

