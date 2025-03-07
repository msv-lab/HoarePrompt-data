#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same backward as forward), otherwise it returns False.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of lowercase Latin characters and returns `True` if `s` is a palindrome (i.e., reads the same backward as forward). If `s` is not a palindrome, it returns `False`. The function does not modify the input string `s`.

#State of the program right berfore the function call: No variables are passed to `func_2()`. Inside the function, `s` is a string consisting of lowercase Latin characters, and `n` is the length of `s` (1 <= n <= 10^6). `x` is an integer initialized to -1.
def func_2():
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: - The `print` statement does not depend on any of the variables or objects mentioned in the initial state. It directly prints the string `'YES'`.
        #
        #Therefore, the output of the code snippet is:
        #Output:
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: s (where s is a string consisting of lowercase Latin characters)
        return
        #The program returns `None`.
    #State: *`s` is a string consisting of lowercase Latin characters, `n` is the length of `s`, `x` is -1, and `func_1(s[0:])` returns True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: If `s` contains any character different from `s[0]` at any position `i` (where `1 <= i < n`), then `x` will be the index of the first such character. Otherwise, `x` will remain -1. The string `s` and the length `n` will remain unchanged.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns without any value.
    #State: If `s` contains any character different from `s[0]` at any position `i` (where `1 <= i < n`), then `x` will be the index of the first such character. Otherwise, `x` will remain -1. The string `s` and the length `n` will remain unchanged. Additionally, `x` is not equal to -1.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: [s[:x + 1]] [s[x + 1:]] (where [s[:x + 1]] is the substring from the start of `s` up to and including the first character different from `s[0]`, and [s[x + 1:]] is the substring from the position immediately after `x` to the end of `s`)
    else :
        if (x == 1 or x == n // 2) :
            print('NO')
            #This is printed: NO
        else :
            print('YES')
            #This is printed: YES
            print(2)
            #This is printed: - The `print` statement is straightforward and does not depend on any variables or conditions from the precondition.
            #   - The integer `2` is printed directly.
            #
            #Given the above analysis, the output of the `print` statement is:
            #
            #Output:
            print(s[:x + 2], ' ', s[x + 2:])
            #This is printed: s[:x + 2] ' ' s[x + 2:] (where s[:x + 2] is the substring from the start up to and including the character at index x + 1, and s[x + 2:] is the substring starting from the character at index x + 2 to the end)
        #State: *If `s` contains any character different from `s[0]` at any position `i` (where `1 <= i < n`), then `x` will be the index of the first such character. Otherwise, `x` will remain -1. The string `s` and the length `n` will remain unchanged. Additionally, `x` is not equal to -1, and `func_1(s[x + 1:])` returns `True`. If `x` is 1 or `n // 2`, the condition `x == 1 or x == n // 2` is true. Otherwise, `x` is not equal to 1 and `x` is not equal to `n // 2`.
    #State: *If `s` contains any character different from `s[0]` at any position `i` (where `1 <= i < n`), then `x` will be the index of the first such character. Otherwise, `x` will remain -1. The string `s` and the length `n` will remain unchanged. Additionally, `x` is not equal to -1. If `func_1(s[x + 1:])` returns `False`, then `x` is the index of the first character in `s` that is different from `s[0]` and `func_1(s[x + 1:])` returns `False`. If `func_1(s[x + 1:])` returns `True`, then `x` is the index of the first character in `s` that is different from `s[0]`, and `x` is either 1 or `n // 2` if the condition `x == 1 or x == n // 2` is true, otherwise `x` is not equal to 1 and `x` is not equal to `n // 2`.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads a string `s` from the user input, where `s` consists of lowercase Latin characters and has a length `n` (1 <= n <= 10^6). The function checks if the string `s` meets certain conditions by calling another function `func_1`. If `func_1(s)` returns `False`, the function prints 'YES', followed by the integer `1` and the string `s`, and then returns `None`. If `func_1(s)` returns `True`, the function searches for the first character in `s` that is different from the first character. If all characters in `s` are the same, it prints 'NO' and returns without any value. If a different character is found at index `x`, the function further checks `func_1(s[x + 1:])`. If `func_1(s[x + 1:])` returns `False`, it prints 'YES', followed by the integer `2` and the substrings `s[:x + 1]` and `s[x + 1:]`. If `func_1(s[x + 1:])` returns `True`, it prints 'NO' if `x` is 1 or `n // 2`, otherwise it prints 'YES', followed by the integer `2` and the substrings `s[:x + 2]` and `s[x + 2:]`. In all cases, the function either returns `None` or returns without any value.

