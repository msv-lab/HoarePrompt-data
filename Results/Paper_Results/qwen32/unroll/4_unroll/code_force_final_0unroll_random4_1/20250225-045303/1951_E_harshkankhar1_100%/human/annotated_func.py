#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string `s` is a palindrome, otherwise it returns False.
#Overall this is what the function does:The function checks if the input string `s` is a palindrome and returns `True` if it is, otherwise it returns `False`.

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
        #This is printed: s (where s is the input string provided by the user)
        return
        #The program returns None
    #State: `s` is the input string provided by the user, `n` is the length of the string `s`, and `x` is -1. The function `func_1(s[0:])` returns `True`.
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: `s` is the input string provided by the user, `n` is the length of the string `s`, and `x` is the index of the first character in `s` that is different from `s[0]`, or -1 if all characters in `s` are the same.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing (None)
    #State: `s` is the input string provided by the user, `n` is the length of the string `s`, and `x` is the index of the first character in `s` that is different from `s[0]`. `x` is not -1, indicating that there is at least one character in `s` that is different from the first character.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: aaaa bbb
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
            #This is printed: s[:x + 2] s[x + 2:] (where s[:x + 2] includes the first x + 2 characters of s and s[x + 2:] includes the rest of the characters starting from index x + 2)
        #State: `s` is the input string provided by the user, `n` is the length of the string `s`, and `x` is the index of the first character in `s` that is different from `s[0]`. `x` is not -1, indicating that there is at least one character in `s` that is different from the first character. Additionally, `func_1(s[x + 1:])` returns True. If `x` is 1 or `n // 2`, the current value of `x` is either 1 or `n // 2`. Otherwise, `x` is neither 1 nor `n // 2`.
    #State: `s` is the input string provided by the user, `n` is the length of the string `s`, and `x` is the index of the first character in `s` that is different from `s[0]`. `x` is not -1, indicating that there is at least one character in `s` that is different from the first character. If `func_1(s[x + 1:])` is `False`, then the result of `func_1(s[x + 1:])` is `False`. Otherwise, `func_1(s[x + 1:])` returns `True`, and `x` is either 1, `n // 2`, or neither 1 nor `n // 2`.
#Overall this is what the function does:The function `func_2` reads a string `s` from the user, checks certain conditions based on the characters in the string, and prints specific messages and values depending on those conditions. The function always returns `None`.

