#State of the program right berfore the function call: password is a string of length 1 <= n <= 20, where each character is either a lowercase Latin letter or a digit.
def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
        
    #State: After all iterations of the loop, `password` is processed such that all its digits are collected into the `digits` list, and all its letters are collected into the `letters` list.
    digits.sort()
    letters.sort()
    for i in range(len(digits)):
        if i < len(digits) - 1 and digits[i] > digits[i + 1]:
            return False
        
        if i < len(letters) and digits[-1] > letters[i]:
            return False
        
    #State: Output State: The `letters` list is a sorted list, `i` is equal to the length of `digits`, and `digits` is a list. No conditions inside the loop have triggered a return statement, meaning that the loop has completed all its iterations without encountering any breaking conditions. Therefore, the function has successfully iterated over all elements in `digits` (and `letters` up to index `i-1`), and no early returns have been made based on the given conditions.
    sortedPassword = ''.join(digits + letters)
    if (sortedPassword == password) :
        return True
        #The program returns True
    else :
        return False
        #The program returns False
#Overall this is what the function does:The function `func_1` accepts a password string and processes it by separating digits and letters into two lists. It then sorts these lists. If the sorted combination of digits and letters matches the original password and certain conditions are met (no adjacent digits are out of order and no digit is greater than the last letter), the function returns True. Otherwise, it returns False.

