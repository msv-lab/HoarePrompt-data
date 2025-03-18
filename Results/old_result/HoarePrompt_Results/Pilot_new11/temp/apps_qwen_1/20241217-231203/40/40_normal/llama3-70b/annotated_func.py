#State of the program right berfore the function call: The input is a non-empty string consisting of lowercase English letters with a length at most 50.
def func():
    s = input()
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if substr != substr[::-1]:
                max_len = max(max_len, len(substr))
        
    #State of the program after the  for loop has been executed: `max_len` is the maximum length of any substring in `s` that is not a palindrome, `i` is the final value of `i` after the loop completes, `j` is the final value of `j` after the loop completes, and `s` is the original string.
    print(max_len if max_len > 0 else 0)
#Overall this is what the function does:The function accepts a non-empty string consisting of lowercase English letters with a length at most 50. It then iterates through all possible substrings of the input string to find the longest substring that is not a palindrome. If no such substring exists, it returns 0. After executing the function, the output will be the length of the longest non-palindromic substring found, or 0 if no such substring exists.

