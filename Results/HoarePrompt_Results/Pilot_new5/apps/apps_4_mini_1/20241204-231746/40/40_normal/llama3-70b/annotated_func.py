#State of the program right berfore the function call: s is a non-empty string consisting of lowercase English letters with a length of at most 50 characters.
def func():
    s = input()
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if substr != substr[::-1]:
                max_len = max(max_len, len(substr))
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string with length `n`, `max_len` is the length of the longest substring of `s` that is not a palindrome, `n` is a positive integer.
    print(max_len if max_len > 0 else 0)
#Overall this is what the function does:The function accepts a non-empty string `s` consisting of lowercase English letters and calculates the length of the longest substring of `s` that is not a palindrome. If all substrings are palindromes, it returns 0. The function prints the result but does not return a value directly.

