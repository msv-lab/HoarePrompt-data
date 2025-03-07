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
    #State: `n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, `digits` is a list containing all the digits from `password`, and `letters` is sorted.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, `digits` is a list containing all the digits from `password`, `letters` is sorted, and `digits` is sorted.
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: The loop does not modify the variables `n`, `password`, `letters`, or `digits`. The loop checks if there is any position in the string `password` where a letter is immediately followed by a digit. If such a position is found, the loop returns 'NO'. If no such position is found, the loop completes all iterations without returning anything, and the variables remain unchanged.
    return 'YES'
    #The program returns 'YES' if no position in the string `password` has a letter immediately followed by a digit.
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a string `password` of length `n` (where 1 <= n <= 20 and `password` consists of lowercase Latin letters and digits). It returns 'NO' if the letters in `password` are not sorted, if the digits in `password` are not sorted, or if any letter in `password` is immediately followed by a digit. Otherwise, it returns 'YES'.

