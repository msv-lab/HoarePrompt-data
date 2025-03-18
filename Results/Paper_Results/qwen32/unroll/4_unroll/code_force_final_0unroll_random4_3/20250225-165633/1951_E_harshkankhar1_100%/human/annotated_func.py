#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome, otherwise it returns False.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin characters and returns `True` if `s` is a palindrome; otherwise, it returns `False`.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters, and x is an integer that is initially set to -1.
def func_2():
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: s (where s is the string provided by user input)
        return
        #The program returns None
    #State: `s` is a string provided by user input, `n` is the length of `s`, `x` is -1, and `func_1(s[0:])` returns `True`
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: `s` is the same string provided by user input, `n` is the same length of `s`, `x` is the index of the first character in `s` that is different from `s[0]` if such a character exists, otherwise `x` is -1, and `i` is `n` if no differing character is found, otherwise `i` is the index of the first differing character.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: `s` is the same string provided by user input, `n` is the same length of `s`, `x` is the index of the first character in `s` that is different from `s[0]`, and `i` is the index of the first differing character. `x` is not equal to -1.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: Based on the analysis, the print statement will output the integer `2`.
        #
        #Output:
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: aaaaa  bbb
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
            #This is printed: the substring from the start of s to the character at index x + 1, followed by a space, and then the substring from the character at index x + 2 to the end of s
        #State: `s` is the same string provided by user input, `n` is the same length of `s`, `x` is the index of the first character in `s` that is different from `s[0]`, and `i` is the index of the first differing character. `x` is not equal to -1, and `func_1(s[x + 1:])` returns `True`. Additionally, `x` is either 1 or `n // 2`, or `x` is neither 1 nor `n // 2`.
    #State: `s` is the same string provided by user input, `n` is the same length of `s`, `x` is the index of the first character in `s` that is different from `s[0]`, and `i` is the index of the first differing character. `x` is not equal to -1. If `func_1(s[x + 1:])` returns `False`, then the function proceeds accordingly. Otherwise, if `func_1(s[x + 1:])` returns `True`, then `x` is either 1 or `n // 2`, or `x` is neither 1 nor `n // 2`.
#Overall this is what the function does:The function reads a string `s` from user input and checks certain conditions based on the characters in the string and the results of an external function `func_1`. It prints either 'YES' or 'NO' along with additional information depending on these conditions. The function does not return any value (it returns `None`).

