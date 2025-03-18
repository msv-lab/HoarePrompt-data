#State of the program right berfore the function call: The function `func_1` is expected to take two parameters, `n` and `k`, where `n` is an integer representing the length of the strings to be considered, and `k` is an integer representing the number of the first lowercase English alphabets to use. Both `n` and `k` are within the range 1 ≤ n, k ≤ 26. The function should handle multiple test cases, indicated by an integer `t` (1 ≤ t ≤ 676), where each test case provides a new pair of `n` and `k`.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that consists of the first `k` characters of the string 'abcdefghijklmnopqrstuvw' repeated `n` times, where `n` and `k` are integers between 1 and 26.
#Overall this is what the function does:The function `func_1` reads two integers, `n` and `k`, from the input, where `1 ≤ n, k ≤ 26`. It then constructs a string consisting of the first `k` characters of the string 'abcdefghijklmnopqrstuvw' repeated `n` times. The function returns this constructed string.

