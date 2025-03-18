#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same backward as forward), otherwise it returns False.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin characters and returns `True` if the string is a palindrome (reads the same backward as forward), otherwise it returns `False`.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters, and n is the length of the string s such that 1 ≤ n ≤ 10^6.
def func_2():
    s = input()
    n, x = len(s), -1
    if (func_1(s[0:]) == False) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(s)
        #This is printed: s
        return
        #The program does not return any value
    #State: s is an input string, n is the length of the input string s, x is -1, and func_1(s[0:]) is True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: The value of `i` is `n-1`, `x` is either -1 or the index where the first non-matching character is found (if such an index exists), and `n` is the length of the input string `s`.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: The value of `i` is `n-1`, `x` is either -1 or the index where the first non-matching character is found (if such an index exists), and `n` is the length of the input string `s`. Since the if condition `(x == -1)` is false, `x` is not -1 and there exists at least one non-matching character in the string `s`.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: s[:x + 1] [space] s[x + 1:]
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
            #This is printed: the substring from the start of the string up to and including the index x + 1, followed by a space, and then the substring starting from the index x + 2 to the end of the string
        #State: Postcondition: `i` is `n-1`, `x` is the index where the first non-matching character is found, and `n` is the length of the input string `s`. If `x` is either 1 or half the length of the string `s`, then no change is made to `x`. Otherwise, `x` remains the index where the first non-matching character is found.
    #State: Postcondition: `i` is `n-1`, `x` is the index where the first non-matching character is found, and `n` is the length of the input string `s`. If `func_1(s[x + 1:])` returns `False`, then no change is made to `x`. Otherwise, if `x` is either 1 or half the length of the string `s`, then no change is made to `x`. In all other cases, `x` remains the index where the first non-matching character is found.
#Overall this is what the function does:The function reads an input string `s` and determines whether it can be split into two non-empty substrings such that both substrings are palindromes. If such a split exists, it prints "YES" followed by the indices or substrings involved in the split. If no such split exists, it prints "NO". The function does not return any value.

