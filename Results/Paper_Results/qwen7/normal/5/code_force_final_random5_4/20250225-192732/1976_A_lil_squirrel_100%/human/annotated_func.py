#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, and password is a string of length n consisting of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: The `letters` list contains all characters from the `password` string that are not digits, and the `digits` list contains all characters from the `password` string that are digits.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: The `letters` list contains all characters from the `password` string that are not digits, and the `digits` list contains all characters from the `password` string that are digits. The `letters` list is not sorted.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: The `letters` list contains all characters from the `password` string that are not digits, and the `digits` list contains all characters from the `password` string that are digits. The `letters` list is not sorted, and the `digits` list is sorted.
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: Output State: The variable `i` is equal to `len(password) - 1`, and neither the `return` statement within the loop has been executed, meaning no 'NO' has been returned. All characters in the `letters` list are unsorted as they were initially, and all characters in the `digits` list remain sorted as they were initially. The `password` string has been fully iterated over without any condition inside the loop being met to return 'NO'.
    #
    #This means that after all iterations of the loop, the function has gone through each possible pair of adjacent characters in the `password` string (from the first character to the second last character), checking if the current character is alphabetic and the next character is a digit. Since the function did not encounter such a pair, it means that no alphabetic character was followed immediately by a digit in the `password` string.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function accepts two parameters: `n`, an integer between 1 and 20 (inclusive), and `password`, a string of length `n` consisting of lowercase Latin letters and digits. It checks if the `password` string meets certain conditions. If any of the following conditions are true, it returns 'NO':
1. The list of letters in the password is not sorted alphabetically.
2. The list of digits in the password is not sorted numerically.
3. There is at least one occurrence where an alphabetic character is immediately followed by a digit.
If none of these conditions are met, it returns 'YES'.

