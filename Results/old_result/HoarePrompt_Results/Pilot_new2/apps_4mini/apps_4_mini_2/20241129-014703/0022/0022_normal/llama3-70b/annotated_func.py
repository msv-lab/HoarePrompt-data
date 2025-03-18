#State of the program right berfore the function call: s is a string consisting of English letters with a length between 1 and 1000.
def func():
    s = input()
    n = len(s)
    is_spalindrome = True
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            is_spalindrome = False
            break
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of English letters with a length between 1 and 1000; `n` is the length of `s`; `is_spalindrome` is True if `s` is a palindrome, otherwise it is False.
    print('TAK' if is_spalindrome else 'NIE')
#Overall this is what the function does:The function accepts a string input from the user, checks if it is a palindrome, and prints 'TAK' if it is, or 'NIE' if it is not. The function does not validate the input to ensure it consists only of English letters or meets the length requirement.

