#State of the program right berfore the function call: password is a string consisting of lowercase Latin letters and digits, with a length of 1 to 20 characters.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: digits is a list containing all the digits from the string password, and letters is a list containing all the lowercase Latin letters from the string password.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: `digits` is a list containing all the digits from the string `password`, `letters` is a list containing all the lowercase Latin letters from the string `password`, `last_digit_index` is the index of the last digit in `password` or -1 if no digit is found.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'.
    #State: *`digits` is a list containing all the digits from the string `password`, `letters` is a list containing all the lowercase Latin letters from the string `password`, `last_digit_index` is the index of the last digit in `password` or -1 if no digit is found, and `digits` is sorted in non-decreasing order.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'.
    #State: *`digits` is a list containing all the digits from the string `password`, `letters` is a list containing all the lowercase Latin letters from the string `password`, `last_digit_index` is the index of the last digit in `password` or -1 if no digit is found, `digits` is sorted in non-decreasing order, and `letters` is sorted in non-decreasing order.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts a string `password` consisting of lowercase Latin letters and digits, with a length of 1 to 20 characters. It returns 'NO' if any digit appears after a letter in the string or if the digits or letters in the string are not in non-decreasing order. Otherwise, it returns 'YES'.

