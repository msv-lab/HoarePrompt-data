#State of the program right berfore the function call: l is an integer such that 1 <= l <= n, and x is an integer such that 1 <= x <= 10^9.
def func_1(l, x):
    print(f'? {l} {x}')
    #This is printed: ? [l] [x] (where [l] is an integer between 1 and n, and [x] is an integer between 1 and 10^9)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns the input integer `ret`.
#Overall this is what the function does:The function `func_1` takes two parameters, `l` and `x`, where `l` is an integer between 1 and n, and `x` is an integer between 1 and 10^9. It prints a query string in the format "? [l] [x]" to the standard output, flushes the output buffer, reads an integer from the standard input, and returns this integer. After the function concludes, the program state includes the returned integer `ret`.

#State of the program right berfore the function call: m is an integer representing the largest value such that the array can be split into exactly k subarrays where the product of the length and the maximum of each subarray equals m, or -1 if no such m exists.
def func_2(m):
    print(f'! {m}')
    #This is printed: ! [m] (where [m] is the largest value such that the array can be split into exactly k subarrays where the product of the length and the maximum of each subarray equals m, or -1 if no such m exists)
    sys.stdout.flush()
    ret = int(input())
#Overall this is what the function does:The function `func_2` accepts an integer `m` and prints it prefixed by "! ". It then reads an integer from the standard input and returns this integer. The function does not modify the value of `m` or any other external state. The returned value is expected to be `m` if it meets certain conditions (as described in the comments), or -1 otherwise, but the function itself does not enforce these conditions; it simply returns whatever integer is provided through the input.

#State of the program right berfore the function call: n and k are positive integers such that 1 <= k <= n <= 10^4.
def func_3():
    n, k = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        
        if r <= n:
            assert r == n
            max_val = i
            break
        
    #State: `n` and `k` are positive integers such that \(1 \leq k \leq n \leq 10^4\), `max_val` is the largest integer `i` such that `func_1(1, i * n)` returns a value `r` where `r` is less than or equal to `n` and `r` equals `n`. If no such `i` exists, `max_val` remains 0.
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
        
    #State: After the loop executes all iterations, `n` and `k` remain the same, with `k` being greater than or equal to 1. `max_val` remains the same. `i` is 0, as the loop decrements `i` from `n // k` down to 1 and then stops. `m` is 0, because `m` is calculated as `i * max_val` and `i` is 0. `p` is the final value obtained from the repeated application of `func_1` starting from `p = 1` and incrementing by 1 each time, until `p` becomes greater than or equal to `n` or the loop completes all `k` iterations. `j` is the final value of the loop counter, which will be `k` if the loop completes without breaking due to `p` reaching or exceeding `n`. The loop will terminate without calling `func_2(m)` if `p` never equals `n` for any iteration.
    func_2(-1)
#Overall this is what the function does:The function `func_3` reads two positive integers `n` and `k` from the input, where `1 <= k <= n <= 10^4`. It then attempts to find the largest integer `i` such that `func_1(1, i * n)` returns a value `r` that is equal to `n`. If such an `i` is found, it sets `max_val` to this `i`. Next, it iterates over values of `i` from `n // k` down to 1, calculating `m` as `i * max_val`. For each `m`, it applies `func_1` repeatedly, starting from `p = 1` and incrementing `p` by 1 each time, up to `k` times. If `p` reaches `n`, it calls `func_2(m)` and returns. If no such `m` is found, it calls `func_2(-1)`. The function does not return any value explicitly.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases.
def func_4():
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: `t` must be greater than or equal to the number of iterations, `func_3()` has been called `t` times.
#Overall this is what the function does:The function `func_4` reads an integer `t` from the input, which represents the number of test cases. It then calls the function `func_3` exactly `t` times. The function does not return any value. After the function concludes, `t` remains unchanged, and `func_3` has been executed `t` times.

