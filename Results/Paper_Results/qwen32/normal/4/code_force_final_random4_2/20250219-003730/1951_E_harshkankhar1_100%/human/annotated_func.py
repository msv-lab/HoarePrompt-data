#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome, otherwise it returns False.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin characters and returns `True` if `s` is a palindrome; otherwise, it returns `False`.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters, n is the length of the string s, and x is an integer initialized to -1.
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
    #State: `s` is the input string, `n` is the length of the input string, `x` is -1, and `func_1(s[0:])` returns `True`
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: `s` is the input string, `n` is the length of the input string, `x` is the index of the first character that differs from `s[0]` or -1 if no such character exists, and `func_1(s[0:])` returns `True`.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing (None).
    #State: `s` is the input string, `n` is the length of the input string, `x` is the index of the first character that differs from `s[0]` and `x` is not equal to -1, and `func_1(s[0:])` returns `True`.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: s[:x + 1] s[x + 1:] (where s[:x + 1] includes the first part of the string up to the first differing character, and s[x + 1:] includes the rest of the string)
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
            #This is printed: s[:x + 2], ' ', s[x + 2:] (where s[:x + 2] is the substring from the start of s up to and including the character at index x + 1, and s[x + 2:] is the substring from the character at index x + 2 to the end of s)
        #State: `s` is the input string, `n` is the length of the input string, `x` is the index of the first character that differs from `s[0]` and `x` is not equal to -1, and `func_1(s[0:])` returns `True`. Additionally, `func_1(s[x + 1:])` returns `True`. The current value of `x` is either 1, `n // 2`, or neither.
    #State: `s` is the input string, `n` is the length of the input string, `x` is the index of the first character that differs from `s[0]` and `x` is not equal to -1, `func_1(s[0:])` returns `True`. If `func_1(s[x + 1:])` returns `False`, then `func_1(s[x + 1:])` is `False`. Otherwise, `func_1(s[x + 1:])` is `True` and `x` is either 1, `n // 2`, or neither.
#Overall this is what the function does:The function reads a string `s` from the input, checks certain conditions based on the characters in the string and the result of an external function `func_1`, and prints specific messages and substrings of `s` based on these conditions. The function does not accept any parameters and always returns `None`.

