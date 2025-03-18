#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome, otherwise it returns False.
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
        #This is printed: s (where s is the input string)
        return
        #The program returns None
    #State: *`s` is the input string, `n` is the length of the input string, `x` is -1. The function `func_1(s[0:])` returns True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: `s` is the input string, `n` is the length of the input string, `x` is -1.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: `s` is the input string, `n` is the length of the input string, `x` is not equal to -1.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: s[:x + 1] s[x + 1:] (where s[:x + 1] is the substring from the start of s up to and including the character at index x, and s[x + 1:] is the substring from the character at index x + 1 to the end of s)
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
            #This is printed: the first x+2 characters of s, followed by a space, followed by the rest of the string starting from the character at index x+2
        #State: `s` is the input string, `n` is the length of the input string, `x` is not equal to -1, and `func_1(s[x + 1:])` returns True. If `x` is either 1 or `x` is equal to `n // 2`, then `x` is either 1 or `n // 2`. Otherwise, `x` is neither 1 nor `n // 2`.
    #State: `s` is the input string, `n` is the length of the input string, and `x` is not equal to -1. If `func_1(s[x + 1:])` evaluates to `False`, then `func_1(s[x + 1:])` is `False`. Otherwise, `func_1(s[x + 1:])` returns `True`, and `x` is either 1 or `n // 2` or neither.
#Overall this is what the function does:The function `func_2` reads a string `s` from the input, checks certain conditions based on the characters in the string, and prints specific messages and substrings of `s` based on those conditions. The function always returns `None`.

