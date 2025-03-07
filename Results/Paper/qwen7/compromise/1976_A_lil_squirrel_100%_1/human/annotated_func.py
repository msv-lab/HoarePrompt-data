#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 20, and password is a string of length n consisting of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: Output State: `letters` is a list containing all the lowercase Latin letters from the string `password`, and `digits` is a list containing all the digits from the string `password`.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `letters` is a list containing all the lowercase Latin letters from the string `password`, and `digits` is a list containing all the digits from the string `password`. The list `letters` is already sorted.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `letters` is a list containing all the lowercase Latin letters from the string `password`, and `digits` is a list containing all the digits from the string `password`. The list `digits` is already sorted.
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: Output State: `letters` is a list containing all the lowercase Latin letters from the string `password`, and `digits` is a list containing all the digits from the string `password`. The list `digits` is already sorted, and the loop has executed all iterations without finding any alphabetic character followed immediately by a digit.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer between 1 and 20 (inclusive), and `password`, a string of length `n` consisting of lowercase Latin letters and digits. It separates the characters in `password` into two lists: one for letters and one for digits. The function then checks if both lists are sorted and ensures there are no alphabetic characters followed immediately by digits. If these conditions are met, the function returns 'YES'; otherwise, it returns 'NO'.

