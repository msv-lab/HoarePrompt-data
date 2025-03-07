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
        #This is printed: s (where s is the input string)
        return
        #The program does not return any value
    #State: s is an input string, n is the integer value calculated from `len(s)`, `x` is -1, and `func_1(s)` returns `True`
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: Output State: s is an input string, n is the integer value calculated from `len(s)`, `x` is either -1 or the index of the first character in `s` that does not match the first character, and `func_1(s)` returns `True`.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value
    #State: `s` is an input string, `n` is the integer value calculated from `len(s)`, `x` is the index of the first character in `s` that does not match the first character, and `func_1(s)` returns `True`.
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: s[:x + 1] s[x + 1:]
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
            #This is printed: s[:x + 2] s[x + 2:]
        #State: `s` is an input string, `n` is the integer value calculated from `len(s)`, `x` is the index of the first character in `s` that does not match the first character, and `func_1(s)` returns `True`. The substring `s[x + 1:]` contains at least one character that matches the first character of `s`. If `x` is either 1 or half the length of `s` (rounded down), then no change occurs. Otherwise, `x` remains unchanged.
    #State: Postcondition: `s` is an input string, `n` is the integer value calculated from `len(s)`, `x` is the index of the first character in `s` that does not match the first character, and `func_1(s)` returns `True`. If the substring starting from index `x + 1` of `s` does not satisfy the condition `func_1`, then no change occurs. If the substring `s[x + 1:]` contains at least one character that matches the first character of `s` and `x` is either 1 or half the length of `s` (rounded down), then no change occurs. Otherwise, `x` remains unchanged.
#Overall this is what the function does:The function processes an input string `s` and checks certain conditions related to the string. It does not return any value. Depending on the conditions met, it prints one of two messages ('YES' or 'NO') along with some indices or substrings of the input string. The function also calls another function `func_1` which is not detailed here but assumed to return a boolean value.

