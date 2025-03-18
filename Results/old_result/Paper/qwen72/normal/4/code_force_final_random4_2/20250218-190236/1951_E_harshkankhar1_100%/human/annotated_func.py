#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same backward as forward), or False if it is not.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of lowercase Latin characters and returns `True` if `s` is a palindrome (i.e., reads the same backward as forward). If `s` is not a palindrome, it returns `False`. The function does not modify the input string `s`.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters, and its length n is such that 1 <= n <= 10^6.
def func_2():
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: - The `print` statement does not depend on any of the variables or objects described in the initial state. It simply prints the string `'YES'`.
        #
        #Therefore, the output of the code snippet is:
        #Output:
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: s (where s is a string consisting of lowercase Latin characters and its length n is between 1 and 10^6)
        return
        #The program returns `None`.
    #State: `s` is a string consisting of lowercase Latin characters as input by the user, `n` is the length of `s` (1 <= n <= 10^6), `x` is -1, and `func_1(s[0:])` is True.
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: `s` is a string consisting of lowercase Latin characters as input by the user, `n` is the length of `s` and must be greater than 1, `func_1(s[0:])` is True. If any character in `s` from index 1 to `n-1` is not equal to `s[0]`, `x` is set to the index of the first such character. If all characters from index 1 to `n-1` are equal to `s[0]`, `x` remains -1.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None.
    #State: `s` is a string consisting of lowercase Latin characters as input by the user, `n` is the length of `s` and must be greater than 1, `func_1(s[0:])` is True. `x` is set to the index of the first character in `s` from index 1 to `n-1` that is not equal to `s[0]`.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: s[:x + 1] ' ' s[x + 1:] (where s[:x + 1] is the substring from the start of s up to and including the first character that is different from s[0], and s[x + 1:] is the substring from the first character that is different from s[0] to the end of s)
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
            #This is printed: aabb ' ' cc
        #State: *`s` is a string consisting of lowercase Latin characters as input by the user, `n` is the length of `s` and must be greater than 1, `func_1(s[0:])` is True, `x` is set to the index of the first character in `s` from index 1 to `n-1` that is not equal to `s[0]`, and `func_1(s[x + 1:])` is True. Additionally, if `x` is 1 or `n // 2`, then `x` retains its value. Otherwise, `x` is not equal to 1 and `x` is not equal to `n // 2`.
    #State: `s` is a string consisting of lowercase Latin characters as input by the user, `n` is the length of `s` and must be greater than 1, `func_1(s[0:])` is True, and `x` is set to the index of the first character in `s` from index 1 to `n-1` that is not equal to `s[0]`. If `func_1(s[x + 1:])` is False, then the substring `s[x + 1:]` does not satisfy `func_1`. Otherwise, `func_1(s[x + 1:])` is True, and if `x` is 1 or `n // 2`, then `x` retains its value. If `x` is not 1 and not `n // 2`, then `x` is not equal to 1 and not equal to `n // 2`.
#Overall this is what the function does:The function `func_2` does not accept any parameters and always returns `None`. It reads a string `s` from user input, where `s` consists of lowercase Latin characters and its length `n` is between 1 and 10^6. The function checks if the string `s` satisfies a condition defined by `func_1`. If `func_1(s)` is `False`, it prints `'YES'`, `1`, and the original string `s`, then exits. If `func_1(s)` is `True`, it searches for the first character in `s` (starting from index 1) that is different from the first character of `s`. If all characters are the same, it prints `'NO'` and exits. If a different character is found at index `x`, it checks if the substring `s[x + 1:]` satisfies `func_1`. If `func_1(s[x + 1:])` is `False`, it prints `'YES'`, `2`, and the substrings `s[:x + 1]` and `s[x + 1:]`. If `func_1(s[x + 1:])` is `True`, it prints `'NO'` if `x` is 1 or `n // 2`, otherwise it prints `'YES'`, `2`, and the substrings `s[:x + 2]` and `s[x + 2:]`.

