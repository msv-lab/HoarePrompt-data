#State of the program right berfore the function call: The function `func_1` is expected to take two parameters, `n` and `k`, where `n` is an integer representing the length of the strings to be formed, and `k` is an integer representing the number of the first lowercase English alphabets to be used. Both `n` and `k` are within the range 1 ≤ n, k ≤ 26. The function should also handle multiple test cases, indicated by an integer `t` (1 ≤ t ≤ 676), where each test case provides a pair of `n` and `k`.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string composed of the first `k` characters of the alphabet repeated `n` times. The string 's' is 'abcdefghijklmnopqrstuvw', and the returned string is a substring of 's' from the start up to the `k`-th character, repeated `n` times.
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, where `n` represents the length of the desired string and `k` represents the number of the first lowercase English alphabets to be used. The function then returns a string consisting of the first `k` characters of the alphabet, repeated `n` times. The function does not handle multiple test cases; it processes only one set of `n` and `k` values per call.

