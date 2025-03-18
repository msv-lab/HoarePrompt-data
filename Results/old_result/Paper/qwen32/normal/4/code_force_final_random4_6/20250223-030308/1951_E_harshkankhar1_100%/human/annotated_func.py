#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome, otherwise it returns False.
#Overall this is what the function does:The function checks if the input string `s` is a palindrome and returns `True` if it is, otherwise it returns `False`.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters, n is the length of the string s, and x is an integer used as an index to identify a point in the string s where the character differs from the first character of s.
def func_2():
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: s (where s is the user input string)
        return
        #The program does not return any value.
    #State: `s` is the user input string, `n` is the length of the user input string, `x` is -1, and `func_1(s[0:])` returns True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: x is the index of the first character in `s` that is not equal to `s[0]`, or -1 if no such character exists.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: `x` is the index of the first character in `s` that is not equal to `s[0]`, and `x` is not equal to -1.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: s[:x + 1]  s[x + 1:] (where s[:x + 1] is the substring from the start of s up to and including the first character that is not equal to s[0], and s[x + 1:] is the substring from the character after the first character that is not equal to s[0] to the end of s)
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
            #This is printed: `s[:x + 2]` (which includes `s[0]`, the first character not equal to `s[0]`, and the character immediately following it), a space, and `s[x + 2:]` (the rest of the string starting from the character two positions after the first differing character)
        #State: `x` is the index of the first character in `s` that is not equal to `s[0]`, and `x` is not equal to -1. Additionally, `func_1(s[x + 1:])` returns `True`. The current value of `x` is either 1 or `n // 2`, or `x` is neither 1 nor `n // 2`.
    #State: `x` is the index of the first character in `s` that is not equal to `s[0]`, and `x` is not equal to -1. If `func_1(s[x + 1:])` evaluates to `False`, then `func_1(s[x + 1:])` is `False`. Otherwise, `func_1(s[x + 1:])` returns `True`, and `x` is either 1 or `n // 2`, or `x` is neither 1 nor `n // 2`.
#Overall this is what the function does:The function `func_2` reads a string `s` of lowercase Latin characters and checks for the first character that differs from the first character of the string. Depending on the conditions involving a helper function `func_1`, it prints either 'YES' or 'NO' along with additional information about the string. The function does not return any value.

