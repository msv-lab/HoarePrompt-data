#State of the program right berfore the function call: s is a string consisting of English letters with a length between 1 and 1000.
def func():
    s = input()
    n = len(s)
    is_spalindrome = True
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            is_spalindrome = False
            break
        
    #State of the program after the  for loop has been executed: `s` is an input string, `n` is an integer between 1 and 1000, `is_palindrome` is True if `s` is a palindrome, otherwise False.
    print('TAK' if is_spalindrome else 'NIE')
#Overall this is what the function does:The function accepts an input string `s` consisting of English letters with a length between 1 and 1000 and checks if it is a palindrome. It prints 'TAK' if `s` is a palindrome and 'NIE' if it is not. The function does not return any value; it only prints the result.

