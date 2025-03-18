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
        #This is printed: s (where s is the input string consisting of lowercase Latin characters)
        return
        #The program returns None
    #State: `s` is an input string consisting of lowercase Latin characters, `n` is the length of the input string `s`, and `x` is -1. The function `func_1(s)` returns True.
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: Output State: `s` is an input string consisting of lowercase Latin characters, `n` is the length of the input string `s`, and `x` is either the index of the first character in `s` that does not match the first character, or -1 if all characters in `s` are the same.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: `s` is an input string consisting of lowercase Latin characters, `n` is the length of the input string `s`, and `x` is the index of the first character in `s` that does not match the first character, or -1 if all characters in `s` are the same. In this case, `x` is not equal to -1
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
        #State: Postcondition: `s` is an input string consisting of lowercase Latin characters, `n` is the length of the input string `s`, and `x` is the index of the first character in `s` that does not match the first character, or -1 if all characters in `s` are the same. In this case, `x` is not equal to -1, and `func_1(s[x + 1:])` returns True. If `x` is either 1 or half the length of `s`, the function continues as specified in the if part. Otherwise, the function continues as specified in the else part.
    #State: Postcondition: `s` is an input string consisting of lowercase Latin characters, `n` is the length of the input string `s`, and `x` is the index of the first character in `s` that does not match the first character, or -1 if all characters in `s` are the same. In this case, `x` is not equal to -1. If `func_1(s[x + 1:])` returns False, the function continues as specified in the if part. Otherwise, the function continues as specified in the else part. Specifically, if `x` is either 1 or half the length of `s`, the function continues as specified in the if part. Otherwise, the function continues as specified in the else part.
#Overall this is what the function does:The function reads a string `s` consisting of lowercase Latin characters and determines whether certain conditions are met based on the characters in the string. It prints 'YES' or 'NO' and some indices or substrings of `s` depending on the conditions. The function ultimately returns `None`.

