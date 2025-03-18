#State of the program right berfore the function call: password is a string of length between 1 and 20, inclusive, consisting of lowercase Latin letters and digits.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: All characters from the `password` string have been processed, and `digits` and `letters` lists contain all the digits and lowercase Latin letters from the `password` string, respectively.
    digits.sort()
    letters.sort()
    for i in range(len(digits)):
        if i < len(digits) - 1 and digits[i] > digits[i + 1]:
            return False
        
        if i < len(letters) and digits[-1] > letters[i]:
            return False
        
    #State: Output State: The `letters` list is sorted in ascending order, the `digits` list remains sorted in ascending order, `i` is equal to `len(digits)`, and for every `i` in the range of `len(digits)`, the conditions `i < len(digits) - 1 and digits[i] > digits[i + 1]` are false, and `digits[-1]` is less than or equal to `letters[i]`.
    #
    #This means that after the loop has executed all its iterations, `i` will be equal to the length of the `digits` list. Additionally, the loop has checked that no two consecutive elements in the `digits` list are out of order (i.e., each element is not greater than the next one), and the last element of the `digits` list is not greater than any element in the `letters` list. If any of these conditions were violated during the loop's execution, the function would have returned `False` at the point of violation. Since the function did not return `False`, it implies that all checks passed successfully.
    sortedPassword = ''.join(digits + letters)
    if (sortedPassword == password) :
        return True
        #The program returns True
    else :
        return False
        #The program returns False
#Overall this is what the function does:The function `func_1` accepts a password string consisting of lowercase Latin letters and digits. It sorts the digits and letters within the password separately and then checks if the sorted digits are in non-decreasing order and do not exceed any letter in the sorted letters part. If all checks pass, the function returns `True`; otherwise, it returns `False`.

