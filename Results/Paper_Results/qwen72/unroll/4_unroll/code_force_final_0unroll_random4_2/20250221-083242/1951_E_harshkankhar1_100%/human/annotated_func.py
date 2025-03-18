#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same forwards and backwards), or False if it is not.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of lowercase Latin characters and returns `True` if `s` is a palindrome (reads the same forwards and backwards). If `s` is not a palindrome, it returns `False`.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters, and its length n is a positive integer such that 1 ≤ n ≤ 10^6.
def func_2():
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: s (where s is a string provided by the user with a length between 1 and 1,000,000 characters)
        return
        #The program returns nothing.
    #State: `n` is the length of the string `s`, `x` is -1, and `s` is a string provided by the user with a length `n` such that 1 ≤ n ≤ 10^6. Additionally, `func_1(s[0:])` is true.
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: If `s` contains any character different from `s[0]`, `x` will be the index of the first occurrence of such a character. Otherwise, `x` remains -1. The value of `n` and `s` remain unchanged.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: `s` contains at least one character different from `s[0]`, `x` is the index of the first occurrence of such a character, and the values of `n` and `s` remain unchanged.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: - Since `s` contains at least one character different from `s[0]`, `x` is the index of the first such character.
        #   - `s[:x + 1]` will include all characters from the start of the string up to and including the first character that is different from `s[0]`.
        #   - `s[x + 1:]` will include all characters from the first character that is different from `s[0]` to the end of the string.
        #
        #Given the precondition, the output will be the first part of the string up to and including the first different character, followed by a space, and then the rest of the string.
        #
        #Output:
    else :
        if (x == 1 or x == n // 2) :
            print('NO')
            #This is printed: NO
        else :
            print('YES')
            #This is printed: YES
            print(2)
            #This is printed: 2
            print(s[:x + 2], ' ', s[x + 2:])
            #This is printed: [s[:x + 2]] ' ' [s[x + 2:]] (where [s[:x + 2]] is the substring of s from the start up to and including the character at index x + 1, and [s[x + 2:]] is the substring of s starting from the character at index x + 2 to the end)
        #State: *`s` contains at least one character different from `s[0]`, `x` is the index of the first occurrence of such a character, the values of `n` and `s` remain unchanged, and `func_1(s[x + 1:])` returns `True`. If `x` is either 1 or `n // 2`, then the if part is executed. Otherwise, `x` is neither 1 nor `n // 2`, and the else part is executed.
    #State: *`s` contains at least one character different from `s[0]`, `x` is the index of the first occurrence of such a character, and the values of `n` and `s` remain unchanged. If `func_1(s[x + 1:])` returns `False`, the if part is executed. Otherwise, if `func_1(s[x + 1:])` returns `True`, the else part is executed, and if `x` is either 1 or `n // 2`, the if part is executed. If `x` is neither 1 nor `n // 2`, the else part is executed.
#Overall this is what the function does:The function `func_2` reads a string `s` from the user input, where `s` consists of lowercase Latin characters and has a length `n` such that 1 ≤ n ≤ 10^6. The function checks if the string `s` meets certain conditions using an external function `func_1`. If `func_1(s)` returns `False`, the function prints "YES" followed by "1" and the original string `s`, and then returns. If `func_1(s)` returns `True`, the function searches for the first character in `s` that is different from the first character. If no such character is found, the function prints "NO" and returns. If such a character is found at index `x`, the function further checks the result of `func_1(s[x + 1:])`. If `func_1(s[x + 1:])` returns `False`, the function prints "YES" followed by "2" and the substrings `s[:x + 1]` and `s[x + 1:]` separated by a space, and then returns. If `func_1(s[x + 1:])` returns `True`, the function prints "NO" if `x` is 1 or `n // 2`, otherwise it prints "YES" followed by "2" and the substrings `s[:x + 2]` and `s[x + 2:]` separated by a space, and then returns. In all cases, the function does not return any value.

