#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 20, and password is a string of length n consisting only of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: `n` is an integer such that 1 ≤ n ≤ 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from the `password`, `digits` is a list containing all the digits from the `password`.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is an integer such that 1 ≤ n ≤ 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from the `password`, `digits` is a list containing all the digits from the `password`, and `letters` is sorted
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is an integer such that 1 ≤ n ≤ 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from the `password`, `digits` is a list containing all the digits from the `password`, `letters` is sorted, and `digits` is sorted
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: `n` is an integer such that 1 ≤ n ≤ 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from the `password`, `letters` is sorted, `digits` is a list containing all the digits from the `password`, `digits` is sorted.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` checks if a given password meets specific criteria: it must contain lowercase Latin letters and digits only, the letters must be in alphabetical order, the digits must be in ascending order, and no letter can be immediately followed by a digit. If any of these conditions are not met, the function returns 'NO'; otherwise, it returns 'YES'.

