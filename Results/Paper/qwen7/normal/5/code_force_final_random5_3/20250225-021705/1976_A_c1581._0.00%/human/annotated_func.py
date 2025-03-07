#State of the program right berfore the function call: password is a string consisting of exactly n characters, where 1 <= n <= 20, and each character is either a lowercase Latin letter or a digit.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: All characters from the original `password` string have been processed, and `digits` contains every digit from the `password`, while `letters` contains every character from `password` that is not a digit.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: Output State: The function has executed all iterations of the loop without returning 'NO'. This means that none of the characters in the `password` string are digits, and therefore, `last_digit_index` remains -1.
    #
    #In natural language: After the loop has completed all its iterations, the `last_digit_index` variable still holds the value -1, indicating that no digit was found in the `password` string. The function did not return 'NO' during any iteration, implying that every character in the `password` string is not a digit.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: The `last_digit_index` variable still holds the value -1, indicating that no digit was found in the `password` string. The function did not return 'NO' during any iteration, implying that every character in the `password` string is not a digit. Additionally, the `digits` list is either empty or contains elements that are already sorted.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: The `last_digit_index` variable still holds the value -1, indicating that no digit was found in the `password` string. The function did not return 'NO' during any iteration, implying that every character in the `password` string is not a digit. Additionally, the `digits` list is either empty or contains elements that are already sorted. The `letters` list is sorted.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts a password string and checks if it contains any digits. If the password contains any digits, the function returns 'NO'. If the password consists solely of lowercase Latin letters, the function further checks if the letters and digits (if any) are sorted. If both the letters and digits (if present) are sorted, the function returns 'YES'; otherwise, it returns 'NO'.

