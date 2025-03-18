#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 20, and password is a string of length n consisting only of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: `n` is a positive integer such that 1 <= n <= 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the characters from `password` that are not digits, and `digits` is a list containing all the characters from `password` that are digits.`
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is a positive integer such that 1 <= n <= 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the characters from `password` that are not digits, and `digits` is a list containing all the characters from `password` that are digits. The list `letters` is sorted.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is a positive integer such that 1 <= n <= 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the characters from `password` that are not digits, and `digits` is a list containing all the characters from `password` that are digits. The list `letters` is sorted, and the list `digits` is sorted.
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: `n` is a positive integer such that 1 <= n <= 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the characters from `password` that are not digits, and `digits` is a list containing all the characters from `password` that are digits. Both `letters` and `digits` are sorted. The loop has completed all its iterations without returning 'NO'.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` checks if a given password meets specific criteria. It returns 'YES' if the password contains all its letters in sorted order, all its digits in sorted order, and no letter is immediately followed by a digit. Otherwise, it returns 'NO'.

