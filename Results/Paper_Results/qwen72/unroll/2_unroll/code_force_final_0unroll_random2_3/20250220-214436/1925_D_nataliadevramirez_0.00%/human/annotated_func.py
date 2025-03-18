#State of the program right berfore the function call: n is an integer representing the number of children, m is an integer representing the number of friend pairs, k is an integer representing the number of excursions, and friendships is a list of tuples where each tuple contains three integers (a, b, f) representing the indices of the children who are friends and their initial friendship value. The values satisfy 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), 1 ≤ k ≤ 2 * 10^5, 1 ≤ a, b ≤ n, a ≠ b, and 1 ≤ f ≤ 10^9.
def func_1(n, m, k, friendships):
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: n remains unchanged, m remains unchanged, k remains unchanged, friendships remains unchanged, result is the sum of (f * (k * (k + 1) // 2) % MOD) for each friendship (a, b, f) in the friendships list.
    return result % MOD
    #The program returns the result of (the sum of (f * (k * (k + 1) // 2) % MOD) for each friendship (a, b, f) in the friendships list) % MOD.
#Overall this is what the function does:The function `func_1` accepts four parameters: `n` (the number of children), `m` (the number of friend pairs), `k` (the number of excursions), and `friendships` (a list of tuples where each tuple contains the indices of two children and their initial friendship value). It calculates the sum of the product of each friendship value `f` and the triangular number of `k`, modulo `MOD`. The function returns this final sum, also modulo `MOD`. The input parameters `n`, `m`, `k`, and `friendships` remain unchanged after the function execution.

#State of the program right berfore the function call: No variables in the function signature.
def func_2():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: The variable `t` is unchanged. For each iteration, `n`, `m`, `k`, and `friendships` are updated based on user input, and the result of `func_1(n, m, k, friendships)` is printed. After all iterations, `t` remains the same as the initial state, but the values of `n`, `m`, `k`, and `friendships` are not retained and are re-assigned in each iteration.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads an integer `t` from user input, which represents the number of test cases. For each test case, it reads three integers `n`, `m`, and `k`, followed by `m` lines of friendship data. It then calls `func_1` with `n`, `m`, `k`, and the friendship data, and prints the result of `func_1`. After processing all test cases, the variable `t` remains unchanged, but the values of `n`, `m`, `k`, and `friendships` are not retained between iterations.

