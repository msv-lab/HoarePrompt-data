#State of the program right berfore the function call: The input is a non-empty string of length at most 50 characters, containing only lowercase English letters.
def func():
    s = input()
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if substr != substr[::-1]:
                max_len = max(max_len, len(substr))
        
    #State of the program after the  for loop has been executed: `max_len` is the length of the longest palindromic substring found in `s`, `substr` is the longest palindromic substring found in `s`, `i` is `n`, `n` is the length of `s`.
    print(max_len if max_len > 0 else 0)
#Overall this is what the function does:The function accepts a non-empty string of length at most 50 characters and prints the length of the longest palindromic substring found in the string, or `0` if no palindromic substring is present.

