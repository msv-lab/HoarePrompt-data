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
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string containing only lowercase English letters, `n` is equal to the length of `s`, `max_len` is the length of the longest non-palindromic substring of `s`. `max_len` will be 0 if all substrings of `s` are palindromic.
    print(max_len if max_len > 0 else 0)
#Overall this is what the function does:The function accepts a non-empty string `s` consisting only of lowercase English letters (length up to 50) and calculates the length of the longest substring that is not a palindrome. If all substrings of `s` are palindromic, the function returns 0. However, the way the function operates does not adequately handle the case where there might be no non-palindromic substrings, especially when all characters in the string are the same; it could mistakenly assume there are non-palindromic substrings when there are not. In summary, it identifies the maximum length of non-palindromic substrings and outputs that length or 0 if none exist.

