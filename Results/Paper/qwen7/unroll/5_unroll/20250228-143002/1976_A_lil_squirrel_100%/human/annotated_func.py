#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, and password is a string of length n consisting of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: Output State: `letters` is a list containing all the lowercase Latin letters from the string `password`, `digits` is a list containing all the digits from the string `password`, `n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting of lowercase Latin letters and digits.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `letters` is a list containing all the lowercase Latin letters from the string `password`, `digits` is a list containing all the digits from the string `password`, `n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting of lowercase Latin letters and digits, and the list `letters` is sorted
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `letters` is a list containing all the lowercase Latin letters from the string `password`, `digits` is a list containing all the digits from the string `password`, `n` is an integer such that 1 <= n <= 20, `password` is a string of length n consisting of lowercase Latin letters and digits, and the list `digits` is sorted
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: Output State: `letters` is a list containing all the lowercase Latin letters from the string `password`, `digits` is a list containing all the digits from the string `password`, and the loop has executed without encountering any lowercase letter followed immediately by a digit, so it did not return 'NO'.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function accepts two parameters: `n`, an integer between 1 and 20 (inclusive), and `password`, a string of length `n` consisting of lowercase Latin letters and digits. It separates the characters in `password` into two lists: one for letters and one for digits. The function then checks if both lists are sorted and ensures there are no instances where a letter is immediately followed by a digit. If any of these conditions are not met, the function returns 'NO'. Otherwise, it returns 'YES'.

