#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, and password is a string of length n consisting only of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: `n` is an integer such that 1 <= n <= 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password` in the order they appear, and `digits` is a list containing all the digits from `password` in the order they appear.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is an integer such that 1 <= n <= 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password` in the order they appear, and `digits` is a list containing all the digits from `password` in the order they appear. Additionally, the list `letters` is sorted in non-decreasing order.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is an integer such that 1 <= n <= 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password` in the order they appear, and `digits` is a list containing all the digits from `password` in the order they appear. Additionally, the list `letters` is sorted in non-decreasing order, and the list `digits` is sorted in non-decreasing order.
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: The loop completes all iterations without returning 'NO'. The state of `n`, `password`, `letters`, and `digits` remains unchanged as per the initial conditions.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` checks if a given password, consisting of lowercase Latin letters and digits, meets specific criteria: all letters must be in non-decreasing order, all digits must be in non-decreasing order, and no letter should be immediately followed by a digit. It returns 'YES' if the password meets all these criteria, otherwise it returns 'NO'.

