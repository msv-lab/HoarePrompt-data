#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, and password is a string of length n consisting of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: Output State: `n` is an integer such that 1 <= n <= 20, and `password` is a string of length n consisting of lowercase Latin letters and digits; `letters` is a list containing all non-digit characters from `password`; `digits` is a list containing all digit characters from `password`.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is an integer such that 1 <= n <= 20, and `password` is a string of length n consisting of lowercase Latin letters and digits; `letters` is a list containing all non-digit characters from `password`; `digits` is a list containing all digit characters from `password`. The first element of `letters` is equal to the last element of `letters`
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `n` is an integer such that 1 <= n <= 20, and `password` is a string of length n consisting of lowercase Latin letters and digits; `letters` is a list containing all non-digit characters from `password`; `digits` is a list containing all digit characters from `password`. The first element of `letters` is equal to the last element of `letters`. The list `digits` is sorted
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: Output State: `n` is an integer such that 1 <= n <= 20, and `password` is a string of length n consisting of lowercase Latin letters and digits; `letters` is a list containing all non-digit characters from `password`; `digits` is a list containing all digit characters from `password`; the first element of `letters` is equal to the last element of `letters`; `digits` is sorted; the loop has executed all iterations without returning 'NO'.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function accepts two parameters: `n`, an integer where 1 <= n <= 20, and `password`, a string of length `n` consisting of lowercase Latin letters and digits. It separates the password into letters and digits, checks if the first and last letters are the same, if the digits are sorted, and if there are no adjacent characters where a letter is followed immediately by a digit. If any of these conditions fail, the function returns 'NO'. Otherwise, it returns 'YES'.

