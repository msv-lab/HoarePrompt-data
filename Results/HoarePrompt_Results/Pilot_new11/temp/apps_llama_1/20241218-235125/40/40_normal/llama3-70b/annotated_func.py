#State of the program right berfore the function call: The function takes no explicit input parameters, but it is expected to read a non-empty string s from the standard input, where s has a length of at most 50 characters and contains only lowercase English letters.
def func():
    s = input()
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if substr != substr[::-1]:
                max_len = max(max_len, len(substr))
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string with a length of at most 50 characters, containing only lowercase English letters, `n` is an integer between 1 and 50 (inclusive), `i` is `n-1`, and `max_len` is the maximum length of all non-palindromic substrings of `s`, or 0 if all substrings are palindromes.
    print(max_len if max_len > 0 else 0)
#Overall this is what the function does:The function reads a string of at most 50 lowercase English letters from the standard input, checks all possible substrings, and prints the maximum length of a non-palindromic substring if one exists; otherwise, it prints 0. The function does not handle cases where the input string is empty or contains non-lowercase English letters, as it assumes the input will always meet the specified criteria. After execution, the program's state includes the input string `s`, its length `n`, the length of the longest non-palindromic substring `max_len` (if any), and the printed result, which is either `max_len` if a non-palindromic substring exists or 0 if all substrings are palindromes. The function does not modify the input string or persist any output beyond printing the result.

