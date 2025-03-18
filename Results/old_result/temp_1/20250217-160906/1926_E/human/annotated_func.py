#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n and k are positive integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        n_back = n
        
        s = (n + 1) // 2
        
        n = (n + 1) // 2
        
        m = 1
        
        while s < k:
            if n == 0:
                s = n_back
                n = 1
                break
            m *= 2
            n //= 2
            s += n
        
        print((2 * (k - (s - n)) - 1) * m)
        
    #State: Output State: `t` test cases are processed, and for each test case, the result is printed based on the given formula. The final state of `t`, `n`, `k`, `n_back`, `s`, `m`, and `n` after all iterations will depend on the input values for each test case, but the output will be a series of integers generated from the formula `(2 * (k - (s - n)) - 1) * m`.
#Overall this is what the function does:The function processes up to 50,000 test cases, where each test case consists of three integers: `n`, `k`, and an implicit `t`. For each test case, it calculates and prints a result based on the formula `(2 * (k - (s - n)) - 1) * m`. After processing all test cases, the function outputs a series of integers corresponding to the calculated results for each test case.

