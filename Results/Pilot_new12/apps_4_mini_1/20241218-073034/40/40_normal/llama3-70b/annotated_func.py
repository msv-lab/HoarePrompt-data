#State of the program right berfore the function call: s is a non-empty string containing only lowercase English letters with a length of at most 50 characters.
def func():
    s = input()
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if substr != substr[::-1]:
                max_len = max(max_len, len(substr))
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string containing only lowercase English letters, `max_len` is the length of the longest non-palindromic substring in `s`, `n` is the length of `s`.
    print(max_len if max_len > 0 else 0)
#Overall this is what the function does:The function reads a non-empty string of lowercase English letters from input, analyzes all possible substrings to determine the length of the longest non-palindromic substring, and prints that length. If all possible substrings are palindromic or if there are no substrings to analyze (which is not the case given the input constraints), it prints 0. It accepts no parameters and operates solely on the internal variable `s`. Additionally, the function does not handle the case where the input string contains only one character—such a string will always result in a maximum length of 0 since there are no non-palindromic substrings possible.

