#State of the program right berfore the function call: s is a string of length between 1 and 1000, consisting of only English letters.**
def func():
    s = input()
    n = len(s)
    is_spalindrome = True
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            is_spalindrome = False
            break
        
    #State of the program after the  for loop has been executed: `s` is a string of length between 1 and 1000, consisting of only English letters; `n` is the length of string `s`, `is_spalindrome` is True if `s` is a palindrome, otherwise False.
    print('TAK' if is_spalindrome else 'NIE')
#Overall this is what the function does:The function `func` reads a string `s` from the input, checks if `s` is a palindrome (reads the same forwards and backwards), and then prints 'TAK' if `s` is a palindrome, and 'NIE' otherwise. The function does not accept any parameters, but operates on the input string `s` of length between 1 and 1000, consisting only of English letters.

