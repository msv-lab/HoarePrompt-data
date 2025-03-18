#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same backward as forward), or False if it is not.
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of lowercase Latin characters and returns `True` if `s` is a palindrome (reads the same backward as forward). If `s` is not a palindrome, it returns `False`. The function does not modify the input string `s`.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters, and its length n is a positive integer such that 1 ≤ n ≤ 10^6.
def func_2():
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: s (where s is the string input by the user with a length between 1 and 10^6)
        return
        #The program returns nothing.
    #State: `s` is a string input by the user, `n` is the length of `s` (a positive integer such that 1 ≤ n ≤ 10^6), `x` is -1, and `func_1(s[0:])` is True.
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: If `s` is a string where all characters are the same as `s[0]`, then `x` remains -1. If `s` contains a character different from `s[0]` at any position `i` (1 ≤ i < n), then `x` is the index of the first occurrence of this different character.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing.
    #State: `s` is a string where not all characters are the same as `s[0]`. `x` is the index of the first occurrence of a character in `s` that is different from `s[0]`, and `x` is not -1.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: - The first part of the output, `s[:x + 1]`, will be the substring from the start of `s` up to and including the first character that is different from `s[0]`.
        #   - The second part of the output, `s[x + 1:]`, will be the remaining part of the string after the first different character.
        #
        #Output:
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
            #This is printed: s[:x + 2] s[x + 2:] (where `s[:x + 2]` is the substring from the start of `s` up to and including the character at index `x + 1`, and `s[x + 2:]` is the substring from the character at index `x + 2` to the end of `s`)
        #State: *`s` is a string where not all characters are the same as `s[0]`. `x` is the index of the first occurrence of a character in `s` that is different from `s[0]`, and `x` is not -1. The substring `s[x + 1:]` satisfies `func_1` (i.e., `func_1(s[x + 1:])` is `True`). If `x` is 1 or `x` is `n // 2`, where `n` is the length of the string `s`, then the function behaves accordingly to the if part. Otherwise, if `x` is not equal to 1 and `x` is not equal to `n // 2`, then the function behaves accordingly to the else part.
    #State: *`s` is a string where not all characters are the same as `s[0]`. `x` is the index of the first occurrence of a character in `s` that is different from `s[0]`, and `x` is not -1. If `func_1(s[x + 1:])` is `False`, the substring `s[x + 1:]` does not satisfy `func_1`. If `func_1(s[x + 1:])` is `True`, the substring `s[x + 1:]` satisfies `func_1`. If `x` is 1 or `x` is `n // 2` (where `n` is the length of the string `s`), the function behaves accordingly to the if part. Otherwise, if `x` is not equal to 1 and `x` is not equal to `n // 2`, the function behaves accordingly to the else part.
#Overall this is what the function does:The function `func_2` reads a string `s` from the user input, where `s` consists of lowercase Latin characters and has a length `n` such that 1 ≤ n ≤ 10^6. It then checks if the string `s` satisfies a condition defined by `func_1`. If `func_1(s)` is `False`, the function prints 'YES', '1', and the string `s`, and then returns. If `func_1(s)` is `True`, the function searches for the first character in `s` that is different from the first character. If all characters are the same, it prints 'NO' and returns. If a different character is found at index `x`, it checks if the substring `s[x + 1:]` satisfies `func_1`. If `func_1(s[x + 1:])` is `False`, it prints 'YES', '2', and the substrings `s[:x + 1]` and `s[x + 1:]`. If `func_1(s[x + 1:])` is `True`, it further checks if `x` is 1 or `n // 2`. If either condition is true, it prints 'NO'. Otherwise, it prints 'YES', '2', and the substrings `s[:x + 2]` and `s[x + 2:]`. In all cases, the function returns nothing.

