#State of the program right berfore the function call: password is a string of length between 1 and 20, inclusive, consisting only of lowercase Latin letters and digits.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: Output State: `password` is a string of length between 1 and 20, inclusive, consisting only of lowercase Latin letters and digits; `digits` is a list containing all the digits from the original `password` in the order they appeared; `letters` is a list containing all the lowercase Latin letters from the original `password` in the order they appeared.
    last_digit_index = -1
    for (i, char) in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return 'NO'
        
    #State: Output State: `last_digit_index` is the index of the last digit in the `password`, `digits` is a list containing all the digits from the original `password` in the order they appeared, `letters` is a list containing all the lowercase Latin letters from the original `password` in the order they appeared.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `last_digit_index` is the index of the last digit in the `password`, `digits` is a list containing all the digits from the original `password` in the order they appeared, `letters` is a list containing all the lowercase Latin letters from the original `password` in the order they appeared, and the `digits` list is sorted
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `last_digit_index` is the index of the last digit in the `password`, `digits` is a list containing all the digits from the original `password` in the order they appeared, `letters` is a list containing all the lowercase Latin letters from the original `password` in the order they appeared, and the `digits` list is sorted. The `letters` list is already sorted.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function accepts a `password` string consisting of lowercase Latin letters and digits. It checks if the digits in the password are in ascending order and the letters are in ascending order. If both conditions are met, it returns 'YES'; otherwise, it returns 'NO'.

