#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 20, and password is a string of length n consisting of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: After the loop executes all the iterations, `n` is a positive integer such that 1 <= n <= 1, `password` is an empty string, `letters` is a list containing all characters from the original `password` that are not digits, and `digits` is a list containing all characters from the original `password` that are digits.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is a positive integer such that 1 <= n <= 1, `password` is an empty string, `letters` is a list containing all characters from the original `password` that are not digits, and `digits` is a list containing all characters from the original `password` that are digits, and `letters` is sorted
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is a positive integer such that 1 <= n <= 1, `password` is an empty string, `letters` is a list containing all characters from the original `password` that are not digits, and `digits` is a list containing all characters from the original `password` that are digits, and `letters` is sorted, and `digits` is sorted
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: Output State: The function has returned 'NO' if it found any instance where a character is alphabetic and the next character is a digit. Otherwise, the function has completed all iterations without returning anything, meaning the `password` remains unchanged and no 'NO' was returned.
    #
    #This means that either the function returned 'NO' during one of its iterations (if it found an alphabetic character followed by a digit), or it went through all characters in the `password` without finding such a pair, thus the `password` remains as it was initially, and 'NO' was never returned.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer between 1 and 20, and `password`, a string of length `n` consisting of lowercase Latin letters and digits. It checks if the `password` meets specific criteria. If it finds an alphabetic character followed by a digit, or if the letters or digits within the password are not sorted, it returns 'NO'. If none of these conditions are met, it returns 'YES'.

