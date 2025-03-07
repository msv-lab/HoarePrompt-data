#State of the program right berfore the function call: password is a string consisting of exactly n characters where each character is either a lowercase Latin letter or a digit, and n is an integer such that 1 ≤ n ≤ 20.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: `digits` contains all the digits from the `password`, and `letters` contains all the lowercase Latin letters from the `password`.
    digits.sort()
    letters.sort()
    for i in range(len(digits)):
        if i < len(digits) - 1 and digits[i] > digits[i + 1]:
            return False
        
        if i < len(letters) and digits[-1] > letters[i]:
            return False
        
    #State: The function completes all iterations without returning False, indicating that the digits are sorted in ascending order and the last digit is not greater than any letter in the letters list.
    sortedPassword = ''.join(digits + letters)
    if (sortedPassword == password) :
        return True
        #The program returns True
    else :
        return False
        #The program returns False
#Overall this is what the function does:The function `func_1` checks if the given password string, consisting of lowercase Latin letters and digits, is already sorted such that all digits come before any letters, both groups are individually sorted in ascending order, and the last digit is not greater than any letter. It returns `True` if these conditions are met; otherwise, it returns `False`.

