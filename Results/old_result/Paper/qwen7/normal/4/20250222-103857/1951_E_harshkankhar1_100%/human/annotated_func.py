#State of the program right berfore the function call: s is a string consisting of lowercase Latin characters.
def func_1(s):
    return s == s[::-1]
    #The program returns True if the string 's' is a palindrome (reads the same backward as forward), otherwise it returns False.
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase Latin characters and returns `True` if `s` is a palindrome (reads the same backward as forward), otherwise it returns `False`.

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
    #State: `s` is an input string, `n` is the length of the input string `s`, `x` is -1, and `func_1(s[0:])` returns True
    for i in range(1, n):
        if s[i] != s[0]:
            x = i
            break
        
    #State: Postcondition: `i` is equal to `n`, `x` is either -1 or the index where the first non-matching character is found (if such an index exists), and the loop has executed `n-1` times.
    if (x == -1) :
        print('NO')
        #This is printed: NO
        return
        #The program does not return any value
    #State: Postcondition: `i` is equal to `n`, `x` is either -1 or the index where the first non-matching character is found (if such an index exists), and the loop has executed `n-1` times. Additionally, the condition `x != -1` holds true.
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
            #This is printed: 'NO'
        else :
            print('YES')
            #This is printed: YES
            print(2)
            #This is printed: 2
            print(s[:x + 2], ' ', s[x + 2:])
            #This is printed: s[:x + 2] s[x + 2:] (where `x` is an index that is neither 1 nor `n // 2`)
        #State: Postcondition: `i` is equal to `n`, `x` is either -1 or the index where the first non-matching character is found (if such an index exists), and the loop has executed `n-1` times. Additionally, the condition `func_1(s[x + 1:]) == True` holds true. **Regardless of whether the condition `x == 1 or x == n // 2` is met, the value of `x` will be either 1, `n // 2`, or neither of these values, while still satisfying the other conditions.**
    #State: Postcondition: `i` is equal to `n`, `x` is either -1 or the index where the first non-matching character is found (if such an index exists), and the loop has executed `n-1` times. Additionally, the condition `x != -1` holds true. Furthermore, if `func_1(s[x + 1:])` returns `False`, `x` remains unchanged. If `func_1(s[x + 1:])` returns `True`, `x` is set to either 1, `n // 2`, or left as -1, ensuring it still satisfies the condition `x != -1`.
#Overall this is what the function does:The function processes an input string `s` and determines whether certain conditions are met based on the string's characters. If the first character of the string is not repeated elsewhere in the string or if specific conditions related to the index `x` are satisfied, it prints 'YES' followed by either 1 or 2 along with relevant substrings. If none of the conditions are met, it prints 'NO'. The function does not return any value.

