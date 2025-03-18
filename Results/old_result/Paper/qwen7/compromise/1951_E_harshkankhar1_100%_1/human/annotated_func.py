#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same backward as forward), otherwise it returns False.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin characters and returns a boolean value. It returns `True` if the string is a palindrome (reads the same backward as forward), otherwise it returns `False`.

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
        #The program returns None
    #State: s is an input string, n is the length of the input string s, x is -1, and func_1(s[0:]) is True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: Output State: s is an input string, n is the length of the input string s, x is the index of the first character in s that is different from the first character of s, and func_1(s[0:]) is True
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value
    #State: s is an input string, n is the length of the input string s, x is the index of the first character in s that is different from the first character of s, and func_1(s[0:]) is True, and x is not equal to -1
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
            #This is printed: "aaaaa" b
        #State: s is an input string, n is the length of the input string s, x is the index of the first character in s that is different from the first character of s, and if x is either 1 or half the length of s, the function continues to check that func_1(s[0:]) is True and func_1(s[x + 1:]) is True. If x is neither 1 nor half the length of s, the function also ensures that func_1(s[0:]) is True and func_1(s[x + 1:]) is True.
    #State: s is an input string, n is the length of the input string s, x is the index of the first character in s that is different from the first character of s, and func_1(s[0:]) is True. If func_1(s[x + 1:]) evaluates to False, the function continues to ensure that func_1(s[0:]) is True and func_1(s[x + 1:]) is True. If x is either 1 or half the length of s, the function checks that both func_1(s[0:]) and func_1(s[x + 1:]) are True. Otherwise, the function also ensures that both func_1(s[0:]) and func_1(s[x + 1:]) are True.
#Overall this is what the function does:The function reads an input string `s` and checks if there is a specific pattern within the string based on certain conditions. If the conditions are met, it prints 'YES' followed by either 1 or 2 and the relevant substrings of `s`. If the conditions are not met, it prints 'NO'. The function does not return any value.

