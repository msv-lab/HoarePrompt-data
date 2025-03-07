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
    #State: *`n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, `digits` is a list containing all the digits from `password`, and `letters` is sorted. Additionally, `digits` is sorted.
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: If the loop completes all iterations without encountering a return statement, the state remains unchanged: `n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, `digits` is a list containing all the digits from `password`, and both `letters` and `digits` are sorted. If the loop encounters a return statement, the function returns 'NO' and the state is not defined beyond this point.
    return 'YES'
    #The program returns 'YES'.
#Overall this is what the function does:The function `func_1` accepts an integer `n` and a string `password` of length `n` (where 1 <= n <= 20 and `password` consists of lowercase Latin letters and digits). It returns 'NO' if any of the following conditions are met: the letters in `password` are not in sorted order, the digits in `password` are not in sorted order, or there is a transition from a letter to a digit in the `password`. If none of these conditions are met, the function returns 'YES'. The function does not modify the input parameters `n` or `password`.

