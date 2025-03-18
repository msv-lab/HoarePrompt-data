#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 20, and password is a string of length n consisting only of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: `n` is a positive integer such that 1 <= n <= 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, `digits` is a list containing all the digits from `password`.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is a positive integer such that 1 <= n <= 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, `digits` is a list containing all the digits from `password`, and `letters` is sorted.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is a positive integer such that 1 <= n <= 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, `digits` is a list containing all the digits from `password`, `letters` is sorted, and `digits` is sorted.
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: n is a positive integer such that 1 <= n <= 20, password is a string of length n consisting only of lowercase Latin letters and digits, letters is a list containing all the lowercase Latin letters from password, sorted, digits is a list containing all the digits from password, sorted.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` checks if a given password, consisting of lowercase Latin letters and digits, meets specific criteria. It returns 'NO' if the lowercase letters or digits in the password are not sorted individually or if a lowercase letter is immediately followed by a digit. Otherwise, it returns 'YES'.

