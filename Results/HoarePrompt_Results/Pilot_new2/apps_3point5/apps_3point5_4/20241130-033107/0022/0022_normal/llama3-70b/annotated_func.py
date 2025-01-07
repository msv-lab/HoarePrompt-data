#State of the program right berfore the function call: s is a string consisting of only English letters with a length between 1 and 1000, inclusive.**
def func():
    s = input()
    n = len(s)
    is_spalindrome = True
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            is_spalindrome = False
            break
        
    #State of the program after the  for loop has been executed: `s` is a palindrome, `n` is the length of `s`, `is_spalindrome` is True. If `s[i] != s[n - i - 1]` for any `i` less than `n // 2`, `is_spalindrome` is False
    print('TAK' if is_spalindrome else 'NIE')
#Overall this is what the function does:The function `func` reads a string `s` consisting of only English letters with a length between 1 and 1000, inclusive. It then checks if the string `s` is a palindrome by comparing characters from the start and end of the string. If the characters do not match, it sets `is_palindrome` to False and breaks the loop. Finally, it prints 'TAK' if `s` is a palindrome, otherwise 'NIE'. The function does not return any value explicitly.

