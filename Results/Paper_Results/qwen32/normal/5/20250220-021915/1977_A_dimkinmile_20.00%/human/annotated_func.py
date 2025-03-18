#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, there are two integers n and m such that 1 <= n, m <= 100.
def func_1():
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: `t` is an integer such that 1 <= t <= 100, and for each of the t test cases, there are two integers `n` and `m` such that 1 <= n, m <= 100. If `n` is greater than or equal to `m`, then `n` is greater than or equal to `m`. Otherwise, `n` is less than `m`.
#Overall this is what the function does:The function reads pairs of integers `n` and `m` from the input for up to 100 test cases and prints "Yes" if `n` is greater than or equal to `m`, otherwise it prints "No".

