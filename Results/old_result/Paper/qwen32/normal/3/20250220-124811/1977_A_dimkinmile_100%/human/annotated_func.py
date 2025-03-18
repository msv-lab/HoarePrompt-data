#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, there are two integers n and m such that 1 <= n, m <= 100.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: `t` is an integer such that 1 <= t <= 100, `n` and `m` are integers read from the input such that 1 <= n, m <= 100. If the difference `n - m` is a non-negative even integer, then the condition `(n - m) % 2 == 0 and n - m >= 0` is true. Otherwise, either `(n - m) % 2 != 0` or `n - m < 0`.
#Overall this is what the function does:The function `func_1` reads two integers `n` and `m` from the input and prints "Yes" if the difference `n - m` is a non-negative even integer, otherwise it prints "No". This process is repeated `t` times, where `t` is the number of test cases provided as input.

