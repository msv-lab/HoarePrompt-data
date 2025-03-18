#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        s = 0
        
        m = 1
        
        while n:
            x = (n + 1) // 2
            n //= 2
            if s < k and k <= s + x:
                break
            s += x
            m *= 2
        
        print((2 * (k - s) - 1) * m)
        
    #State: The loop iterates `t` times, and for each iteration, it reads `n` and `k` from input, performs calculations, and prints a result. After all iterations, `t` is unchanged, and the values of `n` and `k` for the next iteration are undefined (as they are read from input). The variables `s` and `m` are reset to 0 and 1 at the start of each iteration, so their final values are not meaningful after the loop completes.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each of the `t` test cases, it reads two integers `n` and `k` from the input, where 1 ≤ k ≤ n ≤ 10^9. The function performs calculations based on these inputs and prints a result for each test case. After all test cases are processed, the function does not return any value, and the state of the input variables `t`, `n`, and `k` is unchanged. The internal variables `s` and `m` are reset for each test case, so their final values are not meaningful after the function completes.

