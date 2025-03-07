#State of the program right berfore the function call: password is a string consisting of exactly n characters, where each character is either a lowercase Latin letter or a digit.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: Output State: `password` is a string consisting of exactly n characters, where each character is either a lowercase Latin letter or a digit; `digits` is a list containing all the digits from the original `password` string; `letters` is a list containing all the lowercase Latin letters from the original `password` string.
    digits.sort()
    letters.sort()
    for i in range(len(digits)):
        if i < len(digits) - 1 and digits[i] > digits[i + 1]:
            return False
        
        if i < len(letters) and digits[-1] > letters[i]:
            return False
        
    #State: Output State: `password` is a string consisting of characters that are either in non-decreasing order (digits first followed by letters) or all characters are the same. `digits` is a list containing all the digits from the original `password` string sorted in ascending order. `letters` is a list containing all the lowercase Latin letters from the original `password` string sorted in alphabetical order. If the loop returns `False`, it means the `password` does not meet the criteria of having digits and letters in non-decreasing order with digits coming before letters, or all characters being the same.
    sortedPassword = ''.join(digits + letters)
    if (sortedPassword == password) :
        return True
        #The program returns True
    else :
        return False
        #The program returns False
#Overall this is what the function does:The function `func_1` accepts a string `password` consisting of exactly n characters, where each character is either a lowercase Latin letter or a digit. It sorts the digits and letters within the password, checks if the digits are in non-decreasing order and come before any letters, and ensures all characters are either in non-decreasing order or identical. If the password meets these criteria, it returns `True`; otherwise, it returns `False`.

