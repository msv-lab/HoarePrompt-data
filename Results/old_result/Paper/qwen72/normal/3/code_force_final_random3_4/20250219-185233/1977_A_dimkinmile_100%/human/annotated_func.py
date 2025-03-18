#State of the program right berfore the function call: The function `func_1` should actually be defined with parameters `n` and `m`, and the input should be structured such that the first line contains an integer `t` (1 ≤ t ≤ 100) indicating the number of test cases, and each of the following `t` lines contains two integers `n` and `m` (1 ≤ n, m ≤ 100).
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: `n` and `m` are integers with values between 1 and 100. If the difference `(n - m)` is even and non-negative, the condition `(n - m) % 2 == 0 and n - m >= 0` holds true. Otherwise, either `(n - m) % 2 != 0` or `n - m < 0` is true.
#Overall this is what the function does:The function `func_1` reads two integers `n` and `m` from the input, where `1 ≤ n, m ≤ 100`. It checks if the difference `(n - m)` is even and non-negative. If the condition is true, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value. After the function concludes, the program state is such that the input values `n` and `m` have been processed and the appropriate message has been printed based on the condition.

