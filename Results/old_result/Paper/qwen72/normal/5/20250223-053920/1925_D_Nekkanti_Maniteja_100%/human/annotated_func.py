#State of the program right berfore the function call: The function `func` is intended to solve a problem involving multiple test cases, each with the number of children `n`, the number of pairs of friends `m`, and the number of excursions `k`. The input for each test case includes `n`, `m`, and `k` as integers, where `2 ≤ n ≤ 10^5`, `0 ≤ m ≤ min(10^5, n(n-1)/2)`, and `1 ≤ k ≤ 2 * 10^5`. Additionally, for each of the `m` pairs, there are three integers `a_i`, `b_i`, and `f_i` representing the indices of the children in the pair and their initial friendship value, with `1 ≤ a_i, b_i ≤ n`, `a_i ≠ b_i`, and `1 ≤ f_i ≤ 10^9`. The function should handle up to `5 * 10^4` test cases, with the sum of `n` and `m` over all test cases not exceeding `10^5` and the sum of `k` not exceeding `2 * 10^5`.
def func():
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        M = 10 ** 9 + 7
        
        c = pow(n * (n - 1) // 2, -1, M)
        
        s = 0
        
        a = 0
        
        for i in range(m):
            u, v, f = map(int, input().split())
            a += f
        
        for i in range(k):
            s = s + c * i * c * m + c * a
        
        print(s % M)
        
    #State: The function will print the result of `s % M` for each test case, where `s` is the cumulative sum of the expression `s + c * i * c * m + c * a` over `k` iterations, and `c` is the modular inverse of `n * (n - 1) // 2` modulo `10^9 + 7`. The variables `n`, `m`, `k`, `M`, `c`, `s`, and `a` will be reset for each test case, and the final state of these variables for each test case will be the state immediately after the last iteration of the inner `k` loop.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `m`, and `k`, and a list of `m` pairs of integers `a_i`, `b_i`, and `f_i`. For each test case, it calculates a cumulative sum `s` based on the modular inverse of `n * (n - 1) // 2` modulo `10^9 + 7`, the number of pairs `m`, and the sum of friendship values `a`. The final result for each test case is `s % M`, where `M` is `10^9 + 7`, and this result is printed. The function does not return any values; it only prints the results. The variables `n`, `m`, `k`, `M`, `c`, `s`, and `a` are reset for each test case, and their final state is the state immediately after the last iteration of the inner `k` loop.

