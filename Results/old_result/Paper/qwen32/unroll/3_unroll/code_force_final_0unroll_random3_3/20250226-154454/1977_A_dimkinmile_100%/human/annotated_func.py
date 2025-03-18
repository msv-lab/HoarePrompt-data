#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n and m are integers such that 1 <= n, m <= 100.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: `t` is an integer such that 1 <= t <= 100; `n` and `m` are integers as read from the input, where 1 <= n, m <= 100. If `n - m` is even and non-negative, then the condition `n - m % 2 == 0 and n - m >= 0` is true. Otherwise, `n - m` is either not divisible by 2 or is less than 0.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads two integers `n` and `m` from the input for each of `t` test cases. For each test case, it prints 'Yes' if the difference `n - m` is even and non-negative; otherwise, it prints 'No'.

