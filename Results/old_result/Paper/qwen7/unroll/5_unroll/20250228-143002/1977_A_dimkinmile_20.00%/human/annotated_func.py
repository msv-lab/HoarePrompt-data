#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
def func_1():
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 100, `n` is an input integer, `m` is an input integer. If `n` is greater than or equal to `m`, then no changes are made to `n`. If `n` is less than `m`, then no changes are made to `n` either.
#Overall this is what the function does:The function processes a test case consisting of two positive integers `n` and `m` (where 1 ≤ n, m ≤ 100). Based on whether `n` is greater than or equal to `m`, it prints either 'Yes' or 'No'. The function does not return any value but prints the result directly.

