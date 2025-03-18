#State of the program right berfore the function call: l is an integer such that 1 <= l <= n, and x is an integer such that 1 <= x <= 10^9.
def func_1(l, x):
    print(f'? {l} {x}')
    #This is printed: ? [l] [x] (where 1 <= l <= n and 1 <= x <= 10^9)
    sys.stdout.flush()
    ret = int(input())
    return ret
    #The program returns the integer value of `ret`.
#Overall this is what the function does:The function `func_1` accepts two parameters, `l` and `x`, where `l` is an integer between 1 and n, and `x` is an integer between 1 and 10^9. It prints a query string in the format `? [l] [x]` to the standard output and then reads an integer input from the standard input. The function returns this integer value.

#State of the program right berfore the function call: m is an integer representing the largest value such that the array can be split into k subarrays where each subarray's product of length and maximum value equals m, or -1 if no such m exists.
def func_2(m):
    print(f'! {m}')
    #This is printed: ! [m] (where [m] is the largest value such that the array can be split into k subarrays where each subarray's product of length and maximum value equals m, or -1 if no such m exists)
    sys.stdout.flush()
    ret = int(input())
#Overall this is what the function does:The function `func_2` takes an integer `m` as input and prints it in a specific format. It then reads an integer from standard input and returns this integer. The function does not modify the input `m` but uses it to determine the format of the printed message. The returned value is determined by the user's input and is not directly related to the input `m`.

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
        
    #State: After all iterations of the loop, `n` is a positive integer such that \(1 \leq k \leq n \leq 10^4\), `i` is 0, and `max_val` is the largest integer \(i\) such that `func_1(1, i * n)` is less than or equal to `n`. If no such \(i\) exists, `max_val` remains 0.
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
        
    #State: After all iterations of the loop, `n` is a positive integer such that \(1 \leq k \leq n \leq 10^4\), `i` is 0, `max_val` is the largest integer \(i\) such that `func_1(1, i * n)` is less than or equal to `n` (if no such \(i\) exists, `max_val` remains 0), `m` is `0 * max_val` (which is 0), `p` is the final value after all iterations of the inner loop, which is `func_1(p + 1, m)` for each iteration until `p` is greater than or equal to `n` or `j` reaches `k`, `j` is `k`, `k` is greater than or equal to 1, and `p` is not equal to `n` unless the loop breaks because `p` becomes greater than or equal to `n`.
    func_2(-1)
#Overall this is what the function does:The function `func_3` reads two positive integers `n` and `k` from the input, where \(1 \leq k \leq n \leq 10^4\). It then attempts to find a specific value `m` such that a series of calls to `func_1` results in a value `p` that equals `n`. If such a value `m` is found, it calls `func_2(m)`. If no such value is found, it calls `func_2(-1)`. The function does not return any value.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases.
def func_4():
    t = int(input())
    for _ in range(t):
        func_3()
        
    #State: `t` is 0.
#Overall this is what the function does:The function `func_4` reads an integer `t` from the user input, which represents the number of test cases. It then iterates `t` times, calling the function `func_3` in each iteration. After completing all iterations, the value of `t` is unchanged. The function does not return any value.

