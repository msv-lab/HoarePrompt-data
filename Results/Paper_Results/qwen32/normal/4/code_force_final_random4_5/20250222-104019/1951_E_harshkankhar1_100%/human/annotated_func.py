#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome, otherwise it returns False.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin characters and returns `True` if `s` is a palindrome, otherwise it returns `False`.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters, n is the length of s, and x is an integer initialized to -1.
def func_2():
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: s (where s is the input string)
        return
        #The program returns None
    #State: `s` is the input string, `n` is the length of the input string, `x` is -1, and `func_1(s[0:])` returns True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: `s` is the input string, `n` is the length of the input string, `x` is either the index of the first character in `s` (starting from index 1) that is different from `s[0]`, or `-1` if no such character exists, and `func_1(s[0:])` returns True.
    #
    #In simpler terms, `x` will be the index of the first character in `s` (other than the first character) that is different from `s[0]`, or `-1` if all characters in `s` are the same.
    #
    #Output State:
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: `s` is the input string, `n` is the length of the input string, `x` is either the index of the first character in `s` (starting from index 1) that is different from `s[0]`, or `-1` if no such character exists, and `func_1(s[0:])` returns True. Additionally, `x` is not equal to `-1`, meaning there is at least one character in `s` (other than the first character) that is different from `s[0]`.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: - The `print` statement will output the string `'YES'`.
        #
        #Output:
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: s[:x + 1] s[x + 1:] (where s[:x + 1] is the substring from the start of s up to and including the first character different from s[0], and s[x + 1:] is the substring from the first character different from s[0] to the end of s)
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
            #This is printed: s[:x + 2] s[x + 2:] (where s[:x + 2] includes the first differing character and the character after it, and s[x + 2:] includes all characters after the character after the first differing character)
        #State: `s` is the input string, `n` is the length of the input string, `x` is the index of the first character in `s` (starting from index 1) that is different from `s[0]`. Additionally, `func_1(s[0:])` returns True and `func_1(s[x + 1:])` returns True. If `x` is either 1 or `n // 2`, the conditions specified in the if part hold. Otherwise, `x` is neither 1 nor `n // 2`.
    #State: `s` is the input string, `n` is the length of the input string, `x` is the index of the first character in `s` (starting from index 1) that is different from `s[0]`, and `func_1(s[0:])` returns True. Additionally, `x` is not equal to `-1`, meaning there is at least one character in `s` (other than the first character) that is different from `s[0]`. If `func_1(s[x + 1:])` is False, then the current value of `func_1(s[x + 1:])` is False. Otherwise, `func_1(s[x + 1:])` is True. If `x` is either 1 or `n // 2`, the conditions specified in the if part hold. Otherwise, `x` is neither 1 nor `n // 2`.
#Overall this is what the function does:The function `func_2` reads an input string `s` and checks for the presence of a character different from the first character. Depending on the result of this check and further conditions, it prints either 'YES' or 'NO' along with additional information about the string. The function always returns `None`.

