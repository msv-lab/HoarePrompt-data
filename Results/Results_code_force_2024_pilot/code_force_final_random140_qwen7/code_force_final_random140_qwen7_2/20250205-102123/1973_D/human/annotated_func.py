#State of the program right berfore the function call: l is an integer such that 1 <= l <= n, and x is an integer such that 1 <= x <= 10^9.
def func_1(l, x):
    print(f'? {l} {x}')
    #This is printed: ? [l] [x]
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns the integer value of `ret`
#Overall this is what the function does:The function `func_1` accepts two parameters, `l` and `x`, where `l` is an integer between 1 and `n` inclusive, and `x` is an integer between 1 and 10^9 inclusive. It prints a query in the format "? [l] [x]" to the standard output, flushes the output buffer, reads an integer input from the standard input, and returns this integer value.

#State of the program right berfore the function call: m is an integer.
def func_2(m):
    print(f'! {m}')
    #This is printed: ! m (where m is the integer value)
    sys.stdout.flush()
    ret = int(input())
#Overall this is what the function does:The function `func_2` accepts an integer `m` as input. It prints the value of `m` prefixed with '!', reads an integer input from the user, and assigns it to `ret`. The function then returns the value entered by the user. If no valid integer is provided, the behavior depends on the user input.

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
        
    #State: max_val is n, k is an input integer, n must be at least 1.
    for i in range(n // k, 0, -1):
        m = i * max_val
        
        p = 0
        
        for j in range(1, k + 1):
            if p >= n:
                p = 0
                break
            p = func_1(p + 1, m)
        
        if p == n:
            func_2(m)
            return
        
    #State: After all iterations of the loop have finished, `i` will be 0, `max_val` remains unchanged, `m` will be `i * max_val`, `p` will be `n` if the loop conditions were met to execute until `i` reaches 0, otherwise `p` will be the last computed value of `func_1`, `j` will be `k + (n // k - 1)`, and `k` remains unchanged.
    func_2(-1)
#Overall this is what the function does:The function reads two integers \( n \) and \( k \) from the user, where \( 1 \leq k \leq n \leq 10^4 \). It then iterates through values to find a maximum value \( max_val \) such that a certain condition involving \( r \) (calculated using `func_1`) is met. If no such \( max_val \) is found, it proceeds to another loop where it calculates \( m \) and \( p \) using \( max_val \) and \( k \), and calls `func_2` with \( m \) if a specific condition is satisfied. Otherwise, it calls `func_2` with \(-1\). The function can return a value equal to \( n \), return `None`, or not return any value based on the conditions met during its execution.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases. In each test case, n and k are positive integers such that 1 ≤ k ≤ n ≤ 10^4.
def func_4():
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: Output State: `t` must be greater than 0.
    #
    #In natural language: The value of `t` must remain greater than 0 after all the iterations of the loop have finished. This is because the loop continues to execute as long as `t` is greater than 0, and there are no operations within the loop that modify the value of `t`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of two positive integers `n` and `k` such that 1 ≤ `k` ≤ `n` ≤ 10^4. For each test case, it calls another function `func_3()` to process the values of `n` and `k`. After processing all test cases, the function ensures that the variable `t` (representing the number of test cases) remains greater than 0.

