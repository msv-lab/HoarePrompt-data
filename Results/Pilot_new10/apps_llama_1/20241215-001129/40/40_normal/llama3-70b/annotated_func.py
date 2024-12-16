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
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string of length at most 50 characters, containing only lowercase English letters, `n` is the length of `s` and is greater than 0, `i` is equal to `n`, and `max_len` is the length of the longest non-palindrome substring of `s`, or 0 if all substrings of `s` are palindromes.
    print(max_len if max_len > 0 else 0)
#Overall this is what the function does:The function accepts a string, finds the length of the longest non-palindrome substring, and prints it; if all substrings are palindromes, it prints 0, assuming the input string is non-empty and contains only lowercase English letters.

