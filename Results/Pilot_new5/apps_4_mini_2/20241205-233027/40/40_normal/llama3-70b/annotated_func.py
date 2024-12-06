#State of the program right berfore the function call: s is a non-empty string of lowercase English letters with length at most 50.
def func():
    s = input()
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if substr != substr[::-1]:
                max_len = max(max_len, len(substr))
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string of lowercase English letters with length at most 50, `n` is a positive integer between 1 and 50, `max_len` is the length of the longest non-palindromic substring in `s`.
    print(max_len if max_len > 0 else 0)
#Overall this is what the function does:The function accepts a non-empty string `s` and calculates the length of the longest non-palindromic substring. It prints this length, returning 0 if all substrings are palindromic.

