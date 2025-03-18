#State of the program right berfore the function call: password is a string of length 1 <= n <= 20, where each character is either a lowercase Latin letter or a digit.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: All characters from the original `password` have been processed, and the variables `letters` and `digits` contain all the letters and digits from the original `password`, respectively.
    digits.sort()
    letters.sort()
    for i in range(len(digits)):
        if i < len(digits) - 1 and digits[i] > digits[i + 1]:
            return False
        
        if i < len(letters) and digits[-1] > letters[i]:
            return False
        
    #State: Output State: The loop has executed all iterations without returning False, meaning that for every `i` in the range of `len(digits)`, the following conditions hold:
    #- `i` is less than `len(digits) - 1` and `digits[i]` is less than or equal to `digits[i + 1]`.
    #- For all `i` where `i` is less than `len(letters)`, `digits[-1]` is less than or equal to `letters[i]`.
    #
    #This means the loop completes all its iterations without finding any pair of consecutive elements in `digits` that are out of order, and also ensures that the last element of `digits` is not greater than any element in `letters`.
    sortedPassword = ''.join(digits + letters)
    if (sortedPassword == password) :
        return True
        #The program returns True
    else :
        return False
        #The program returns False
#Overall this is what the function does:The function `func_1` accepts a password string and sorts its digits and letters separately. It then checks if the sorted digits are non-decreasing and if the last digit is not greater than any letter in the password. If both conditions are met, the function returns `True`; otherwise, it returns `False`.

