#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 1 ≤ n ≤ 20 for each testcase, and password is a string of length n consisting only of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an integer such that 1 ≤ n ≤ 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, and `digits` is a list containing all the digits from `password`.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an integer such that 1 ≤ n ≤ 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, and `digits` is a list containing all the digits from `password`. The list `letters` is sorted.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is an integer such that 1 ≤ n ≤ 20, `password` is a string of length `n` consisting only of lowercase Latin letters and digits, `letters` is a list containing all the lowercase Latin letters from `password`, and `digits` is a list containing all the digits from `password`. The list `letters` is sorted, and the list `digits` is sorted.
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: t is an integer such that 1 ≤ t ≤ 1000, n is an integer such that 2 ≤ n ≤ 20, password is a string of length n consisting only of lowercase Latin letters and digits, letters is a list containing all the lowercase Latin letters from password, and digits is a list containing all the digits from password. The list letters is sorted, and the list digits is sorted. The loop has completed all iterations without finding a pair where the first character is a lowercase Latin letter and the second is a digit.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function `func_1` checks if a given password meets specific criteria. It returns 'NO' if the password contains unsorted letters, unsorted digits, or if a lowercase Latin letter is immediately followed by a digit. Otherwise, it returns 'YES'.

