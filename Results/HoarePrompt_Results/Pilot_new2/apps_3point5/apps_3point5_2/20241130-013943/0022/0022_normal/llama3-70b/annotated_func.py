#State of the program right berfore the function call: # Precondition
**s is a string of length at least 1 and at most 1000, consisting of only English letters.**
def func():
    s = input()
    n = len(s)
    is_spalindrome = True
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            is_spalindrome = False
            break
        
    #State of the program after the  for loop has been executed: Output State: `s` is a palindrome string of length at least 2 and at most 1000, `n` is the length of `s`, and `is_spalindrome` is True. If `s[i] != s[n - i - 1]` for any i in the range of n//2, then `is_spalindrome` is False.
    print('TAK' if is_spalindrome else 'NIE')
#Overall this is what the function does:The function `func` takes user input for a string `s`, checks if `s` is a palindrome (reads the same forwards and backwards), and prints 'TAK' if it is a palindrome, otherwise prints 'NIE'. The function operates on a string `s` of length at least 1 and at most 1000, consisting of only English letters. If `s` is a palindrome, it sets `is_spalindrome` to True, otherwise False, and outputs the result accordingly.

