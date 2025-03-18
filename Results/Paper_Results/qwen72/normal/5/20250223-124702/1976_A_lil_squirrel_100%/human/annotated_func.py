#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, and password is a string of length n consisting of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: Output State: `n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, `digits` is a list containing all the digits from `password`.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: *`n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, `digits` is a list containing all the digits from `password`, and `letters` is sorted.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'.
    #State: *`n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, `digits` is a list containing all the digits from `password`, `letters` is sorted, and `digits` is sorted.
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: If the loop completes all iterations without encountering a return statement, the state remains unchanged: `n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, `digits` is a list containing all the digits from `password`, `letters` is sorted, and `digits` is sorted. If the loop encounters a return statement, the output is 'NO' and the function exits.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a string `password` of length `n` (where `1 <= n <= 20` and `password` consists of lowercase Latin letters and digits). It returns 'NO' if the letters in `password` are not sorted in non-decreasing order, if the digits in `password` are not sorted in non-decreasing order, or if there is a lowercase letter immediately followed by a digit in `password`. Otherwise, it returns 'YES'.

