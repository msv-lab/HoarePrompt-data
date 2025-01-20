#State of the program right berfore the function call: N is an integer such that 2 <= N <= 5000, and S is a string of length N consisting of lowercase English letters.
def func():
    N = int(input())

S = input()

max_len = 0
    for len in range(1, N // 2 + 1):
        for i in range(N - len):
            substr = S[i:i + len]
            if S.count(substr) > 1 and i + len <= S.index(substr, i + 1):
                max_len = max(max_len, len)
        
    #State of the program after the  for loop has been executed: N is an integer such that 2 <= N <= 5000, S is a string of length N consisting of lowercase English letters, max_len is the maximum length of any substring that appears more than once in S and where the second occurrence starts at or after the end of the first occurrence, len is N // 2, i is N - len. The loop has executed all its iterations, and max_len reflects the largest valid repeating substring length found, or remains 0 if no such substring exists. Variables `N` and `S` remain constant throughout the loop. The loop executes from `len = 1` to `len = N // 2`, and for each `len`, it iterates from `i = 0` to `i = N - len - 1`, checking each substring of length `len` for repeated occurrences that meet the specified conditions.
    print(max_len)
#Overall this is what the function does:The function `func` reads an integer `N` and a string `S` from the standard input, where `N` is the length of `S` and both `N` and `S` meet the constraints provided. It then finds the maximum length of any substring within `S` that appears more than once and where the second occurrence starts at or after the end of the first occurrence. The function prints this maximum length to the standard output. If no such repeating substring exists, it prints `0`. The function does not return any value. The state of the program after the function concludes includes the printed maximum length, and the original values of `N` and `S` remain unchanged. Edge cases include when `S` is a string without any repeating substrings, in which case `0` is printed, and when `S` contains multiple substrings that meet the criteria, in which case the length of the longest one is printed.

