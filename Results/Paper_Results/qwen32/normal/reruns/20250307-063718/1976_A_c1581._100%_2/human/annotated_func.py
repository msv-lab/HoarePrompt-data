#State of the program right berfore the function call: password is a string consisting of exactly n characters, where each character is either a lowercase Latin letter or a digit, and n is an integer such that 1 <= n <= 20.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: password is a string consisting of exactly n characters, where each character is either a lowercase Latin letter or a digit, and n is an integer such that 1 <= n <= 20; digits is a list containing all the digits from the password in the order they appear; letters is a list containing all the lowercase Latin letters from the password in the order they appear.
    digits.sort()
    letters.sort()
    for i in range(len(digits)):
        if i < len(digits) - 1 and digits[i] > digits[i + 1]:
            return False
        
        if i < len(letters) and digits[-1] > letters[i]:
            return False
        
    #State: The loop completes all its iterations without returning False, meaning the last digit in `digits` is not greater than any letter in `letters`. The variable `i` will be equal to `len(digits) - 1`.
    sortedPassword = ''.join(digits + letters)
    if (sortedPassword == password) :
        return True
        #The program returns True
    else :
        return False
        #The program returns False
#Overall this is what the function does:The function checks if a given password, consisting of lowercase Latin letters and digits, is already sorted such that all digits appear before letters, both in ascending order. It returns `True` if the password meets this condition; otherwise, it returns `False`.

