#State of the program right berfore the function call: password is a string consisting of lowercase Latin letters and digits, with a length of 1 to 20 characters.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: `digits` is a list containing all the digits from the string `password`, and `letters` is a list containing all the lowercase Latin letters from the string `password`.
    digits.sort()
    letters.sort()
    for i in range(len(digits)):
        if i < len(digits) - 1 and digits[i] > digits[i + 1]:
            return False
        
        if i < len(letters) and digits[-1] > letters[i]:
            return False
        
    #State: The loop does not modify the `digits` or `letters` lists. The loop checks conditions but does not change the state of the variables. Therefore, `digits` remains a sorted list containing all the digits from the string `password`, and `letters` remains a sorted list containing all the lowercase Latin letters from the string `password`.
    sortedPassword = ''.join(digits + letters)
    if (sortedPassword == password) :
        return True
        #The program returns True.
    else :
        return False
        #The program returns False.
#Overall this is what the function does:The function `func_1` accepts a parameter `password`, which is a string consisting of lowercase Latin letters and digits, with a length of 1 to 20 characters. It separates the digits and letters from the password into two sorted lists. The function returns `True` if the password is already sorted in non-decreasing order of digits followed by non-decreasing order of letters. Otherwise, it returns `False`.

