#State of the program right berfore the function call: The function `func_1` should actually take two parameters, `n` and `k`, where `n` is an integer such that 1 ≤ n ≤ 26, and `k` is an integer such that 1 ≤ k ≤ 26.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that consists of the first `k` characters of 'abcdefghijklmnopqrstuvw' repeated `n` times, where `n` and `k` are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
#Overall this is what the function does:The function `func_1` takes no explicit parameters but reads two integers, `n` and `k`, from the user input. It then returns a string consisting of the first `k` characters of the alphabet (from 'a' to 'w') repeated `n` times. The values of `n` and `k` must be within the range 1 to 26. After the function concludes, the program has returned the constructed string and the input variables `n` and `k` are no longer accessible outside the function.

