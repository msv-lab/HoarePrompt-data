#State of the program right berfore the function call: s is a non-empty string with length at most 50 characters, containing only lowercase English letters.
def func():
    s = input()
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if substr != substr[::-1]:
                max_len = max(max_len, len(substr))
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string of lowercase English letters, `n` is the length of `s`, `max_len` is the length of the longest non-palindromic substring found in `s`, and `i` is `n - 1`, `j` is `n + 1`. If all substrings of `s` are palindromic, `max_len` remains 0.
    print(max_len if max_len > 0 else 0)
#Overall this is what the function does:The function accepts a non-empty string `s` of lowercase English letters, calculates the length of the longest non-palindromic substring, and prints this length or 0 if all substrings are palindromic.

