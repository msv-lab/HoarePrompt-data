#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same backward as forward), otherwise it returns False.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of lowercase Latin characters and returns `True` if `s` is a palindrome (i.e., reads the same backward as forward). If `s` is not a palindrome, it returns `False`. The function does not modify the input string `s`.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters, and n is the length of s such that 1 <= n <= 10^6.
def func_2():
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: s (where s is the string input by the user)
        return
        #The program returns nothing.
    #State: `s` is a string input by the user, `n` is the length of `s` (1 <= n <= 10^6), `x` is -1, and `func_1(s[0:])` is True.
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: `s` is the same string input by the user, `n` is the length of `s`, `x` is the index of the first character in `s` that is different from `s[0]` if such a character exists, otherwise `x` remains -1.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: *`s` is the same string input by the user, `n` is the length of `s`, `x` is the index of the first character in `s` that is different from `s[0]` and `x` is not -1.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: aaab bbccc
    else :
        if (x == 1 or x == n // 2) :
            print('NO')
            #This is printed: - The `print` statement will always print the string 'NO' regardless of the values of `s`, `n`, `x`, or the result of `func_1(s[x + 1:])`.
            #
            #Therefore, based on the given precondition and the code snippet, the output will be:
            #
            #Output:
        else :
            print('YES')
            #This is printed: YES
            print(2)
            #This is printed: 2
            print(s[:x + 2], ' ', s[x + 2:])
            #This is printed: [s[:x + 2]] [s[x + 2:]] (where [s[:x + 2]] is the substring of `s` from the start up to and including the character at index `x + 1`, and [s[x + 2:]] is the substring of `s` starting from the character at index `x + 2` to the end)
        #State: `s` is the same string input by the user, `n` is the length of `s`, `x` is the index of the first character in `s` that is different from `s[0]` and `x` is not -1, and the result of `func_1(s[x + 1:])` is `True`. Additionally, if `x` is either 1 or `n // 2`, this condition is retained. Otherwise, `x` is neither 1 nor `n // 2`.
    #State: *`s` is the same string input by the user, `n` is the length of `s`, and `x` is the index of the first character in `s` that is different from `s[0]` and `x` is not -1. If `func_1(s[x + 1:])` is `False`, the substring `s[x + 1:]` does not satisfy the condition. If `func_1(s[x + 1:])` is `True`, the substring `s[x + 1:]` satisfies the condition, and if `x` is either 1 or `n // 2`, this condition is retained. Otherwise, `x` is neither 1 nor `n // 2`.
#Overall this is what the function does:The function `func_2` reads a string `s` from user input and checks if the string can be split into two substrings such that the second substring does not satisfy the condition checked by `func_1`. If `func_1(s[0:])` returns `False`, it prints 'YES', '1', and the original string `s`, then exits. If all characters in `s` are the same, it prints 'NO' and exits. If `func_1(s[x + 1:])` returns `False` for the first differing character at index `x`, it prints 'YES', '2', and the substrings `s[:x + 1]` and `s[x + 1:]`. If `func_1(s[x + 1:])` returns `True` and `x` is either 1 or `n // 2`, it prints 'NO' and exits. Otherwise, it prints 'YES', '2', and the substrings `s[:x + 2]` and `s[x + 2:]`. In all cases, the function does not return any value.

