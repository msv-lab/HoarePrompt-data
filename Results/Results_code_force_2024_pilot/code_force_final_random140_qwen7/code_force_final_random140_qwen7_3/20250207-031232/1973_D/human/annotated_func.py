#State of the program right berfore the function call: l is an integer such that 1 <= l <= n, and x is an integer such that 1 <= x <= 10^9.
def func_1(l, x):
    print(f'? {l} {x}')
    #This is printed: ? [l] [x]
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns the input integer 'ret'
#Overall this is what the function does:The function `func_1` accepts two parameters, `l` and `x`, where `l` is an integer between 1 and `n` inclusive, and `x` is an integer between 1 and 10^9 inclusive. It prints these values to the standard output, flushes the buffer, reads an integer input from the standard input, and returns this integer.

#State of the program right berfore the function call: m is an integer.
def func_2(m):
    print(f'! {m}')
    #This is printed: ! m (where m is the integer value)
    sys.stdout.flush()
    ret = int(input())
#Overall this is what the function does:The function `func_2` accepts an integer `m` as input. It prints the value of `m` prefixed with '!', reads an integer input from the user, and assigns it to `ret`. If `m` is provided, the function waits for user input. The function does not modify `m` and returns the user-provided integer `ret`. If `m` is not provided (which is not a concern based on the given code), the function would wait for user input.

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
        
    #State: The loop has executed all its iterations. The variable `n` remains as the initial input integer, `i` is now `1` (since the loop decrements `i` from `n` to `1`), `r` is the return value of `func_1(1, (n-1)*n)` (if `i` was `1`), and `max_val` is set to the largest `i` such that `r` is less than or equal to `n` during any iteration of the loop. If no such `i` exists, `max_val` remains `0`.
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
        
    #State: Output State: After the loop executes all its iterations, the variable `i` will be `0` because the loop starts from `n // k` and decrements `i` by `1` in each iteration until it reaches `1`, and then continues decrementing until it becomes `0`. The variable `m` will be `(n // k - 1) * max_val` because `m` is updated in each iteration of the outer loop, and since `i` starts from `n // k` and decreases to `1`, `m` will be updated `n // k - 1` times. The variable `p` will be the result of applying `func_1` exactly `k * (n // k - 1)` times starting from `1` with the updated `m` value, and `p` will not equal `n` unless the loop prematurely returns due to `p >= n` condition being met, but based on the given information, we assume it does not reach `n`. The variable `max_val` will be the largest value of `i` such that `r` (the result of `func_1(1, (n-1)*n)`) is less than or equal to `n` during any iteration, which would be `n // k` since the loop starts from `n // k` and decrements until `0`.
    func_2(-1)
#Overall this is what the function does:The function reads two integers \( n \) and \( k \) from input, where \( 1 \leq k \leq n \leq 10^4 \). It then iterates through values of \( i \) from \( n \) down to 1, calculating \( r \) using the function `func_1(1, i * n)`. If \( r \) is less than or equal to \( n \), it updates `max_val` to \( i \) and breaks out of the loop. Next, it iterates through values of \( i \) from \( n // k \) down to 1, calculating \( m \) as \( i \times max_val \). For each \( i \), it iterates \( k \) times, updating \( p \) using `func_1(p + 1, m)`. If \( p \) equals \( n \) at any point, it calls `func_2(m)` and returns. If no such \( p \) is found, it calls `func_2(-1)` and returns. The function does not return any value.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n and k are positive integers such that 1 ≤ k ≤ n ≤ 10^4.
def func_4():
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: Output State: `t` must be greater than 0.
    #
    #In natural language: The value of `t` must remain greater than 0 after all iterations of the loop have finished. This is because the loop continues to execute as long as `t` is greater than 0, and there are no operations within the loop that modify the value of `t`.
#Overall this is what the function does:The function processes `t` test cases, where for each test case, it accepts two positive integers `n` and `k` such that 1 ≤ `k` ≤ `n` ≤ 10^4. After processing all test cases, it outputs the value of `t`, which must remain greater than 0.

