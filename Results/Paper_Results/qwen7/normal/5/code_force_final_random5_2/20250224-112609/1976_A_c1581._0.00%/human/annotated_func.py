#State of the program right berfore the function call: password is a string of length between 1 and 20, inclusive, consisting of lowercase Latin letters and digits.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: After all iterations, `password` is an empty string, `digits` is a list containing all the digits from the original `password`, and `letters` is a list containing all the lowercase Latin letters from the original `password`.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: The loop will have executed for as many times as there are characters in the password. After all iterations, `last_digit_index` will either be the index of the last digit in the password (if any digits exist), or -1 if no digits are found. The value of `i` will be equal to the length of the password. The function will return 'NO' if a non-digit character is encountered after `last_digit_index` has been set to a positive value.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: The loop will have executed for as many times as there are characters in the password. After all iterations, `last_digit_index` will either be the index of the last digit in the password (if any digits exist), or -1 if no digits are found. The value of `i` will be equal to the length of the password. If `last_digit_index` is set to a positive value, a non-digit character is encountered after `last_digit_index`. The function returns 'NO'.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: The loop will have executed for as many times as there are characters in the password. After all iterations, `last_digit_index` will either be the index of the last digit in the password (if any digits exist), or -1 if no digits are found. The value of `i` will be equal to the length of the password. If `last_digit_index` is set to a positive value, a non-digit character is encountered after `last_digit_index`. The function returns 'YES', and the list `letters` is sorted.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts a string `password` consisting of lowercase Latin letters and digits. It checks if the string meets specific conditions: all digits are in ascending order, and all letters are in alphabetical order. If these conditions are met, it returns 'YES'; otherwise, it returns 'NO'.

