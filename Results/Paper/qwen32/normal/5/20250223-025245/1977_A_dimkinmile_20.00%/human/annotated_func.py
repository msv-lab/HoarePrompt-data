#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n and m are integers such that 1 <= n, m <= 100.
def func_1():
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: `t` is an integer such that 1 <= t <= 100; `n` and `m` are integers read from the input such that 1 <= n, m <= 100. If `n` is greater than or equal to `m`, then `n` is greater than or equal to `m`. Otherwise, `n` is less than `m`.
#Overall this is what the function does:The function reads two integers, `n` and `m`, from the input for each of `t` test cases. It prints "Yes" if `n` is greater than or equal to `m`, and "No" otherwise.

