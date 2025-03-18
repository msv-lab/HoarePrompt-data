#State of the program right berfore the function call: s is a string consisting of English letters with a length between 1 and 1000, inclusive.
def func():
    s = input()
    n = len(s)
    is_spalindrome = True
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            is_spalindrome = False
            break
        
    #State of the program after the  for loop has been executed: `s` is an input string consisting of English letters with a length between 1 and 1000, inclusive; `n` is the length of `s`; `is_spalindrome` is `True` if `s` is a palindrome, `False` otherwise.
    print('TAK' if is_spalindrome else 'NIE')
#Overall this is what the function does:The function accepts no parameters and reads a string input `s` consisting of English letters with a length between 1 and 1000. It checks if the string is a palindrome by comparing characters from the start and end of the string moving towards the center. The function prints 'TAK' if `s` is a palindrome and 'NIE' if it is not. There is no explicit return value from the function, and the result is only printed.

