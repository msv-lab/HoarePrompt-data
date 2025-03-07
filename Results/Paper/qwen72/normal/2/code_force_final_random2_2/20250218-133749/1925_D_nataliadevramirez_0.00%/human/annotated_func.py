#State of the program right berfore the function call: n, m, and k are non-negative integers where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 * 10^5. friendships is a list of m tuples, each containing three integers (a, b, f) where 1 ≤ a, b ≤ n, a ≠ b, and 1 ≤ f ≤ 10^9.
def func_1(n, m, k, friendships):
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: `n`, `m`, and `k` are non-negative integers where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 * 10^5. `friendships` is a list of m tuples, each containing three integers (a, b, f) where 1 ≤ a, b ≤ n, a ≠ b, and 1 ≤ f ≤ 10^9. `result` is the sum of `f * (k * (k + 1) // 2) % MOD` for each tuple (a, b, f) in `friendships`. `i` is `m - 1`, `a` is the first element of the tuple at index `m - 1` of `friendships`, `b` is the second element of the tuple at index `m - 1` of `friendships`, and `f` is the third element of the tuple at index `m - 1` of `friendships`.
    return result % MOD
    #The program returns the final value of `result` modulo `MOD`, which is calculated as the sum of `f * (k * (k + 1) // 2) % MOD` for each tuple (a, b, f) in `friendships`, where `f` is the third element of the last tuple in `friendships`.
#Overall this is what the function does:The function `func_1` takes four parameters: `n`, `m`, `k`, and `friendships`. It processes a list of `m` tuples, each representing a friendship with three integers (a, b, f). The function calculates the sum of `f * (k * (k + 1) // 2) % MOD` for each tuple in `friendships` and returns the final sum modulo `MOD`. After the function concludes, the parameters `n`, `m`, and `k` remain unchanged, and `friendships` is not modified. The function's primary purpose is to compute a specific weighted sum based on the input tuples and return the result modulo `MOD`.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 ≤ t ≤ 5 · 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 · 10^5. friendships is a list of m lists, each containing three integers a_i, b_i, and f_i, where 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and 1 ≤ f_i ≤ 10^9.
def func_2():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: After all iterations of the loop, `t` is 0, and for each iteration, `n`, `m`, and `k` were integers provided by the user input, `friendships` was a list of `m` lists, where each inner list contained integers provided by the user input, and `result` was the value returned by `func_1(n, m, k, friendships)`.
#Overall this is what the function does:The function `func_2` reads multiple test cases from the standard input. For each test case, it reads the values of `n`, `m`, and `k`, followed by `m` lines of friendship data. It then calls another function `func_1` with these parameters and prints the result of `func_1` for each test case. After processing all test cases, the function completes its execution, and the state of the program is such that all input has been processed and the corresponding results have been printed.

