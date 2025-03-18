#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same backward as forward), otherwise it returns False.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of lowercase Latin characters and returns `True` if `s` is a palindrome (i.e., reads the same backward as forward). If `s` is not a palindrome, it returns `False`. The function does not modify the input string `s`.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads a string `s` from the input, where `s` consists of lowercase Latin characters and 1 ≤ |s| ≤ 10^6.
def func_2():
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: s (where s is a string consisting of lowercase Latin characters and 1 ≤ |s| ≤ 10^6)
        return
        #The program returns `None`.
    #State: *`s` is a string consisting of lowercase Latin characters and 1 ≤ |s| ≤ 10^6, `n` is the length of `s`, `x` is -1, and `func_1(s[0:])` is True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: `s` is a string consisting of lowercase Latin characters with 1 ≤ |s| ≤ 10^6, `n` is the length of `s`, `func_1(s[0:])` is True, `i` is `n-1`. If any character in `s` from index 1 to `n-1` is not equal to `s[0]`, `x` is the index of the first such character. Otherwise, `x` remains -1.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: `s` is a string consisting of lowercase Latin characters with 1 ≤ |s| ≤ 10^6, `n` is the length of `s`, `func_1(s[0:])` is True, `i` is `n-1`. There exists at least one character in `s` from index 1 to `n-1` that is not equal to `s[0]`, and `x` is the index of the first such character.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: [s[:x + 1]] [s[x + 1:]] (where [s[:x + 1]] is the substring of `s` from the beginning up to and including the first character that is not equal to `s[0]`, and [s[x + 1:]] is the remaining substring of `s` starting from the first character that is not equal to `s[0]`)
    else :
        if (x == 1 or x == n // 2) :
            print('NO')
            #This is printed: NO
        else :
            print('YES')
            #This is printed: YES
            print(2)
            #This is printed: - The `print` statement will output the integer `2`.
            #
            #Therefore, the final output is:
            #Output:
            print(s[:x + 2], ' ', s[x + 2:])
            #This is printed: - The `print` statement will print the substring `s[:x + 2]` followed by a space and then the substring `s[x + 2:]`.
            #
            #### Example to Illustrate:
            #Suppose `s = "aabbccdd"`.
            #- `n = 8` (length of `s`).
            #- `s[0] = 'a'`.
            #- The first character from index 1 to `n-1` that is not equal to `s[0]` is `s[2] = 'b'`.
            #- Therefore, `x = 2`.
            #- `s[:x + 2] = s[:4] = "aabb"`.
            #- `s[x + 2:] = s[4:] = "ccdd"`.
            #
            #### Final Output:
            #The `print` statement will output the substring `s[:x + 2]` followed by a space and then the substring `s[x + 2:]`.
            #
            #Output:
        #State: *`s` is a string consisting of lowercase Latin characters with 1 ≤ |s| ≤ 10^6, `n` is the length of `s`, `func_1(s[0:])` is True, `i` is `n-1`. There exists at least one character in `s` from index 1 to `n-1` that is not equal to `s[0]`, and `x` is the index of the first such character. `func_1(s[x + 1:])` is True. If `x` is 1 or `n // 2`, then `x` retains its value as 1 or `n // 2`. Otherwise, `x` is not equal to 1 and `x` is not equal to `n // 2`.
    #State: *`s` is a string consisting of lowercase Latin characters with 1 ≤ |s| ≤ 10^6, `n` is the length of `s`, `func_1(s[0:])` is True, `i` is `n-1`. There exists at least one character in `s` from index 1 to `n-1` that is not equal to `s[0]`, and `x` is the index of the first such character. If `func_1(s[x + 1:])` is False, then `func_1(s[x + 1:])` remains False. Otherwise, `func_1(s[x + 1:])` is True, and if `x` is 1 or `n // 2`, then `x` retains its value as 1 or `n // 2`. If `x` is neither 1 nor `n // 2`, then `x` is not equal to 1 and `x` is not equal to `n // 2`.
#Overall this is what the function does:The function `func_2` reads a string `s` from the input, where `s` consists of lowercase Latin characters and its length is between 1 and 1,000,000. It checks if the string `s` satisfies a condition defined by `func_1`. If `func_1(s)` is `False`, the function prints 'YES' followed by '1' and the string `s`, and then returns `None`. If `func_1(s)` is `True`, the function searches for the first character in `s` (starting from index 1) that is different from the first character of `s`. If no such character is found, the function prints 'NO' and returns nothing. If such a character is found at index `x`, the function checks if `func_1(s[x + 1:])` is `False`. If it is `False`, the function prints 'YES' followed by '2', and then the substrings `s[:x + 1]` and `s[x + 1:]`. If `func_1(s[x + 1:])` is `True`, the function further checks if `x` is 1 or `n // 2` (where `n` is the length of `s`). If `x` is 1 or `n // 2`, the function prints 'NO' and returns nothing. Otherwise, the function prints 'YES' followed by '2', and then the substrings `s[:x + 2]` and `s[x + 2:]`.

