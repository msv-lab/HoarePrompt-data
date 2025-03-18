#State of the program right berfore the function call: s is a string consisting of only English letters with a length between 1 and 1000.**
def func():
    s = input()
    n = len(s)
    is_spalindrome = True
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            is_spalindrome = False
            break
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of only English letters with a length between 2 and 1000, `n` is the length of string `s` which is at least 2, `is_spalindrome` is True if the string `s` is a palindrome, False otherwise. `i` is equal to `n // 2` at the end of the loop.
    print('TAK' if is_spalindrome else 'NIE')
#Overall this is what the function does:The function `func` reads an input string `s` consisting of only English letters with a length between 1 and 1000. It then iterates through the string to determine if it is a palindrome. If the string is a palindrome, it prints 'TAK'; otherwise, it prints 'NIE'. The function does not accept any parameters and does not return any value. However, it operates on the input string and prints the result based on whether the string is a palindrome or not.

