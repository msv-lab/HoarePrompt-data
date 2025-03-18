#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, and password is a string of length n consisting only of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: `n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, and `digits` is a list containing all the digits from `password`.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: *`n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, and `digits` is a list containing all the digits from `password`. Additionally, `letters` is sorted.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, and `digits` is a list containing all the digits from `password`. Additionally, `letters` is sorted, and `digits` is sorted.
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: `n` is an integer such that 1 <= n <= 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, and `digits` is a list containing all the digits from `password`. Additionally, `letters` is sorted, and `digits` is sorted, and `n` must be at least 2. The loop has completed all iterations, and there is no position `i` in `password` such that `password[i]` is a lowercase Latin letter and `password[i + 1]` is a digit.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a string `password` of length `n` (where 1 <= n <= 20 and `password` consists only of lowercase Latin letters and digits). It returns 'NO' if any of the following conditions are met: the letters in `password` are not in non-decreasing order, the digits in `password` are not in non-decreasing order, or there is a lowercase letter followed immediately by a digit. If none of these conditions are met, the function returns 'YES'.

