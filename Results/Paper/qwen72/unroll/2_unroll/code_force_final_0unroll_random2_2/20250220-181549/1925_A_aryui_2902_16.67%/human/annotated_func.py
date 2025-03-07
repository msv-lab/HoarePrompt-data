#State of the program right berfore the function call: The function `func_1` is expected to take two positive integers `n` and `k` as input, where 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26. These integers represent the length of the strings to be formed and the number of first lowercase English alphabets to be used, respectively.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that is composed of the first `k` characters of the string 'abcdefghijklmnopqrstuvw' repeated `n` times, where `n` and `k` are positive integers provided by the user input, with 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
#Overall this is what the function does:The function `func_1` accepts two positive integers `n` and `k` (1 ≤ n ≤ 26, 1 ≤ k ≤ 26) from user input and returns a string consisting of the first `k` lowercase English alphabets repeated `n` times. The function does not modify any external state or variables.

