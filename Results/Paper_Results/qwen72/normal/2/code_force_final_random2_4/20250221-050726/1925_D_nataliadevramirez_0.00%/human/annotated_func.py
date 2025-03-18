#State of the program right berfore the function call: n, m, and k are non-negative integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 * 10^5. friendships is a list of tuples, each containing three integers (a, b, f) where 1 ≤ a, b ≤ n, a ≠ b, and 1 ≤ f ≤ 10^9.
def func_1(n, m, k, friendships):
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: `n`, `m`, and `k` are non-negative integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 * 10^5. `friendships` is a list of tuples, each containing three integers (a, b, f) where 1 ≤ a, b ≤ n, a ≠ b, and 1 ≤ f ≤ 10^9. `result` is the sum of `f * (k * (k + 1) // 2) % MOD` for each friendship tuple (a, b, f) in the `friendships` list. `i` is `m - 1`, `m` is greater than or equal to 0, and `a`, `b`, and `f` are the elements at index `m - 1` of the tuple at the last index in the `friendships` list.
    return result % MOD
    #The program returns the result of `result % MOD`, where `result` is the sum of `f * (k * (k + 1) // 2) % MOD` for each friendship tuple (a, b, f) in the `friendships` list, and `MOD` is a constant value not explicitly defined but assumed to be a large integer used for modulo operations.
#Overall this is what the function does:The function `func_1` takes four parameters: `n`, `m`, `k`, and `friendships`. It processes each friendship tuple `(a, b, f)` in the `friendships` list and computes the sum of `f * (k * (k + 1) // 2) % MOD` for each tuple. The final result is the sum of these computations, taken modulo `MOD`. The function returns this final result. The parameters `n`, `m`, and `k` remain unchanged, and the `friendships` list is not modified.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 ≤ t ≤ 5 · 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: After the loop executes all the iterations, `t` is greater than or equal to 0, `n`, `m`, and `k` are input integers, `friendships` is a list of `m` lists, each containing two integers read from the input, and `result` is the value returned by `func_1(n, m, k, friendships)` for each iteration. The loop has executed `t` times, and the final state reflects the results of all `t` test cases.
#Overall this is what the function does:The function `func_2` reads a positive integer `t` indicating the number of test cases to process, where 1 ≤ t ≤ 5 · 10^4. For each test case, it reads three integers `n`, `m`, and `k`, followed by `m` lines of friendship pairs. It then calls another function `func_1` with these inputs and prints the result. After processing all `t` test cases, the function completes, and the final state includes the printed results for each test case.

