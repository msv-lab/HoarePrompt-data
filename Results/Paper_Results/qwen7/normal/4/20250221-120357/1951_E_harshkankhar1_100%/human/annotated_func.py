#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same backward as forward), otherwise it returns False.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin characters and returns `True` if the string is a palindrome (reads the same backward as forward), otherwise it returns `False`.

#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters, and n is the length of s such that 1 ≤ |s| ≤ 10^6.
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
    #State: `s` is an input string, `n` is the length of the input string `s`, `x` is -1, and `func_1(s[0:])` returns True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: The value of `i` is equal to the length of the input string `s`, `n` is the length of the input string `s`, and `x` is either -1 or the index where `s[i]` is not equal to `s[0]` (if such an index exists).
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program returns None
    #State: The value of `i` is equal to the length of the input string `s`, `n` is the length of the input string `s`, and `x` is either -1 or the index where `s[i]` is not equal to `s[0]` (if such an index exists), but `x` is not equal to -1
    if (func_1(s[x + 1:]) == False) :
        print('YES')
        #This is printed: YES
        print(2)
        #This is printed: 2
        print(s[:x + 1], ' ', s[x + 1:])
        #This is printed: s[:x + 1] s[x + 1:] (where s[:x + 1] is the substring from the start of s up to and including the character at index x, and s[x + 1:] is the substring from the character after index x to the end of s)
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
            #This is printed: "abcd" " "
        #State: Postcondition: `i` is equal to the length of the input string `s`, `n` is the length of the input string `s`, `x` is either -1 or the index where `s[i]` is not equal to `s[0]` (if such an index exists), but `x` is not equal to -1, and `func_1(s[x + 1:])` returns True, and `x` is either 1 or half the length of `s` if the condition `(x == 1 or x == n // 2)` is true; otherwise, the condition `(x == 1 or x == n // 2)` is false.
    #State: Postcondition: `i` is equal to the length of the input string `s`, `n` is the length of the input string `s`, and `x` is either -1 or the index where `s[i]` is not equal to `s[0]` (if such an index exists), but `x` is not equal to -1. If `func_1(s[x + 1:])` returns `False`, the condition remains unchanged. Otherwise, `func_1(s[x + 1:])` returns `True`, and `x` is either 1 or half the length of `s` if the condition `(x == 1 or x == n // 2)` is true; otherwise, the condition `(x == 1 or x == n // 2)` is false.
#Overall this is what the function does:The function reads an input string `s` consisting of lowercase Latin characters. It then checks if the string is composed entirely of the same character. If not, it finds the first character that differs from the first character of the string. Based on this, it prints either 'YES' or 'NO', along with additional information. The function returns `None`.

