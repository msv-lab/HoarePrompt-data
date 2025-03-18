#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, and password is a string of length n consisting of lowercase Latin letters and digits.
def func_1(n, password):
    letters = []
    digits = []
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
        
    #State: Output State: After the loop executes all iterations, `password` is a non-empty string of length `n` (where 1 <= n <= 20), `digits` is a list containing all the digits from the `password`, and `letters` is a list containing all the letters from the `password`.
    #
    #In this final state, every character in `password` has been processed, and based on whether each character is a digit or a letter, it has been appended to either the `digits` list or the `letters` list. The order of elements in both lists will correspond to their original order in the `password` string.
    if (letters != sorted(letters)) :
        return 'NO'
        #The program returns 'NO'
    #State: `password` is a non-empty string of length `n` (where 1 <= n <= 20), `digits` is a list containing all the digits from the `password`, and `letters` is a list containing all the letters from the `password`. The letters in `letters` list are in sorted order.
    if (digits != sorted(digits)) :
        return 'NO'
        #The program returns 'NO'
    #State: `password` is a non-empty string of length `n` (where 1 <= n <= 20), `digits` is a list containing all the digits from the `password`, and `letters` is a list containing all the letters from the `password`. The letters in `letters` list are in sorted order, and the `digits` list is sorted.
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return 'NO'
        
    #State: Output State: The function does not return anything.
    #
    #Explanation: After all the iterations of the loop, if the loop did not encounter any situation where `password[i]` is an alphabet and `password[i + 1]` is a digit, it means the condition `if password[i].isalpha() and password[i + 1].isdigit(): return 'NO'` was never met throughout the entire loop execution. Therefore, the function will not return anything and will continue to its next line of code, which in this case is simply ending without returning any value.
    return 'YES'
    #The program returns 'YES'
#Overall this is what the function does:The function accepts two parameters: `n`, an integer where 1 <= n <= 20, and `password`, a string of length `n` consisting of lowercase Latin letters and digits. It separates the characters in `password` into two lists: one for digits and one for letters. If the letters are not in sorted order, or the digits are not in sorted order, or if there is a letter followed immediately by a digit in the `password`, the function returns 'NO'. Otherwise, it returns 'YES'.

