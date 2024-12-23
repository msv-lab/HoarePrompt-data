#State of the program right berfore the function call: s is a non-empty string of lowercase English letters with a length of at most 50 characters.
def func():
    s = input()
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if substr != substr[::-1]:
                max_len = max(max_len, len(substr))
        
    #State of the program after the  for loop has been executed: `s` is the user-input string of lowercase English letters, `n` is the length of `s`, `max_len` is the maximum length of all non-palindromic substrings found in `s`. If all substrings are palindromic, `max_len` will be 0.
    print(max_len if max_len > 0 else 0)
#Overall this is what the function does:The function reads a non-empty string `s` of lowercase English letters from user input and calculates the length of the longest non-palindromic substring found within `s`. After evaluating all possible substrings, it prints the length of the longest non-palindromic substring—returning 0 if all substrings are palindromic. Edge cases include handling the scenario where the input string `s` is a single character (resulting in a maximum length of 0), as well as diverse configurations of characters in `s` that may lead to varying lengths of non-palindromic substrings. The function does not accept parameters, and the string must be input interactively, which could present an inconsistency with the stated parameter in the annotations.

