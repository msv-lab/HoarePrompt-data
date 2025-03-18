#State of the program right berfore the function call: password is a string consisting of exactly n characters, where each character is either a lowercase Latin letter or a digit.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: All characters from the `password` string have been processed, and `digits` contains all the digits from the `password` string while `letters` contains all the non-digit characters.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: The function has either returned 'NO' or `last_digit_index` is equal to the length of the `password` minus one.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: The function has either returned 'NO' or `last_digit_index` is equal to the length of the `password` minus one, and the digits in the `password` are already sorted.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: The function has either returned 'NO', or `last_digit_index` is equal to the length of the `password` minus one, and the digits in the `password` are already sorted, and the letters in the `password` are not sorted.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function accepts a password string and checks if it meets certain criteria. If any of the following conditions are met, it returns 'NO': 1) The password contains a digit that is not the last character; 2) The digits in the password are not sorted in ascending order; 3) The letters in the password are not sorted in ascending order. If none of these conditions are met, it returns 'YES'.

