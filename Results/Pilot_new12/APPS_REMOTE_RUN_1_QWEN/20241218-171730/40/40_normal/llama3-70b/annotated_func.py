#State of the program right berfore the function call: The input is a non-empty string s consisting of lowercase English letters, with a length of at most 50 characters.
def func():
    s = input()
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if substr != substr[::-1]:
                max_len = max(max_len, len(substr))
        
    #State of the program after the  for loop has been executed: `i` is an integer such that `i < n`, `j` is an integer such that `i + 1 <= j <= n`, `s` is a non-empty string, `n` is the length of `s`, `max_len` is the maximum length of any non-palindromic substring found in `s` from index `i` to any valid end index `j` where `i` to `n - 1` and `j` to `n`.
    print(max_len if max_len > 0 else 0)
#Overall this is what the function does:The function accepts a non-empty string `s` consisting of lowercase English letters with a maximum length of 50 characters. It then iterates through all possible substrings of `s` to find the longest non-palindromic substring. If no non-palindromic substring is found, it returns 0. The function prints the length of the longest non-palindromic substring found or 0 if none exists.

