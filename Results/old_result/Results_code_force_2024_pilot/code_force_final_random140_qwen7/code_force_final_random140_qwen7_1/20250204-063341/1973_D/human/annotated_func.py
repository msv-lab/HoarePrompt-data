#State of the program right berfore the function call: l is an integer such that 1 <= l <= n, and x is an integer such that 1 <= x <= 10^9.
def func_1(l, x):
    print(f'? {l} {x}')
    #This is printed: ? [l] [x]
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns the input integer 'ret'
#Overall this is what the function does:The function `func_1` accepts two parameters, `l` and `x`, where `l` is an integer between 1 and `n`, and `x` is an integer between 1 and 10^9. It prints these values and then reads an integer input from the user, which it returns. After the function concludes, the program will have returned the input integer `x`.

#State of the program right berfore the function call: m is an integer.
def func_2(m):
    print(f'! {m}')
    #This is printed: ! m (where m is an integer)
    sys.stdout.flush()
    ret = int(input())
#Overall this is what the function does:The function accepts an integer `m` and reads another integer from the user as input. If `m` is non-negative, it returns the same integer `m`. If `m` is negative, it returns an error message indicating that `m` cannot be negative.

#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ k ≤ n ≤ 10^4.
def func_3():
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: After the loop executes all iterations, `n` is a positive integer, `i` is 1, `r` is the return value of `func_1(1, 1 * n)`, and `max_val` is set to the largest `i` such that `r` is less than or equal to `i * n` for each iteration. If no such `i` exists, `max_val` remains 0.
    for i in range(n // k, 0, -1):
        m = i * max_val
        
        p = 0
        
        for j in range(1, k + 1):
            p = func_1(p + 1, m)
            if p >= n:
                break
        
        if p == n:
            func_2(m)
            return
        
    #State: After the loop executes all iterations, `j` is equal to `k`, `k` is a positive integer, `i` is 0, `r` is the return value of `func_1(1, n)`, `max_val` is the largest `i` such that `r` is less than or equal to `i * n`, `m` is `i * max_val`, and `p` is not equal to `n`.
    func_2(-1)
#Overall this is what the function does:The function accepts no parameters and performs a series of calculations involving `n` and `k`. It iterates through values to find a specific condition where `func_1` returns a value less than or equal to `n`. If such a condition is met, it calls `func_2` with a calculated value `m`. Otherwise, it calls `func_2` with `-1`. The function returns either nothing, `None`, or the value of `p` which is the result of `func_1(k * (p + 1), m)` based on the conditions met during its execution.

#State of the program right berfore the function call: **
def func_4():
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: Output State: `t` must be greater than 0.
    #
    #In natural language: The value of `t` must remain greater than 0 after all the iterations of the loop have finished. This is because the loop continues to execute as long as `t` is greater than 0, and there are no operations within the loop that change the value of `t`.
#Overall this is what the function does:The function reads an integer `t` from the user, which represents the number of times to call `func_3()`. After calling `func_3()` `t` times, the value of `t` must remain greater than 0. The function does not accept any parameters and does not return anything.

