#State of the program right berfore the function call: s is a string consisting of English letters with a length between 1 and 1000, inclusive.
def func():
    s = input()
    n = len(s)
    is_spalindrome = True
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            is_spalindrome = False
            break
        
    #State of the program after the  for loop has been executed: `s` is an input string consisting of English letters, `n` is the length of `s`, `is_spalindrome` is True if `s` is a palindrome and False if it is not.
    print('TAK' if is_spalindrome else 'NIE')
#Overall this is what the function does:The function accepts a string input `s` consisting of English letters and checks if it is a palindrome. If `s` reads the same forwards and backwards, it prints 'TAK'; otherwise, it prints 'NIE'. The function does not handle cases where the input is empty or contains non-English letters, but the problem statement specifies that `s` will have a length between 1 and 1000, so those cases are not expected to occur.

