#State of the program right berfore the function call: password is a string consisting of 1 to 20 characters, where each character is either a lowercase Latin letter or a digit.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: Output State: `digits` is a list containing all the digit characters from the `password` string in the order they appear; `letters` is a list containing all the lowercase Latin letter characters from the `password` string in the order they appear.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: `digits` is a list containing all the digit characters from the `password` string in the order they appear; `letters` is a list containing all the lowercase Latin letter characters from the `password` string in the order they appear; `last_digit_index` is the index of the last digit in the `password` string, or -1 if there are no digits.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: *`digits` is a list containing all the digit characters from the `password` string in the order they appear, and `digits` is sorted in non-decreasing order; `letters` is a list containing all the lowercase Latin letter characters from the `password` string in the order they appear; `last_digit_index` is the index of the last digit in the `password` string, or -1 if there are no digits.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: *`digits` is a list containing all the digit characters from the `password` string in the order they appear, and `digits` is sorted in non-decreasing order; `letters` is a list containing all the lowercase Latin letter characters from the `password` string in the order they appear, and `letters` is sorted in non-decreasing order; `last_digit_index` is the index of the last digit in the `password` string, or -1 if there are no digits.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts a string `password` consisting of 1 to 20 characters, where each character is either a lowercase Latin letter or a digit. It returns 'NO' if any of the following conditions are met: 1) There is a digit followed by a letter in the `password` string, or 2) The digits in the `password` are not in non-decreasing order, or 3) The letters in the `password` are not in non-decreasing order. If none of these conditions are met, the function returns 'YES'.

