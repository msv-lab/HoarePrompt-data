#State of the program right berfore the function call: n is an integer representing the number of children, m is an integer representing the number of friend pairs, k is an integer representing the number of excursions, and friendships is a list of tuples where each tuple contains three integers (a, b, f) representing the indices of two children who are friends and their initial friendship value. The values must satisfy 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), 1 <= k <= 2*10^5, and 1 <= a, b <= n with a != b, 1 <= f <= 10^9.
def func_1(n, m, k, friendships):
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: n remains unchanged, m remains unchanged, k remains unchanged, friendships remains unchanged, result is the sum of (f * (k * (k + 1) // 2) % MOD) for each friendship (a, b, f) in friendships.
    return result % MOD
    #The program returns the sum of (f * (k * (k + 1) // 2) % MOD) for each friendship (a, b, f) in the list `friendships`, modulo MOD.
#Overall this is what the function does:The function `func_1` accepts four parameters: `n` (the number of children), `m` (the number of friend pairs), `k` (the number of excursions), and `friendships` (a list of tuples representing friend pairs and their initial friendship values). It calculates the sum of the product of each friendship value `f` and the triangular number of `k`, modulo a constant `MOD`. The function returns this sum, and the input parameters `n`, `m`, `k`, and `friendships` remain unchanged after the function execution.

#State of the program right berfore the function call: No variables are passed to the function func_2, but it reads inputs from the standard input. The first input is an integer t (1 ≤ t ≤ 5 · 10^4) representing the number of test cases. For each test case, the function reads three integers n, m, and k (2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), 1 ≤ k ≤ 2 · 10^5) representing the number of children, pairs of friends, and excursions, respectively. It then reads m lines, each containing three integers a_i, b_i, and f_i (1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, 1 ≤ f_i ≤ 10^9) representing the indices of the pair of children who are friends and their initial friendship value.
def func_2():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: The value of `t` remains unchanged, and the loop has executed `t` times. Each execution of the loop reads `n`, `m`, and `k` from input, reads `m` lines of friendship data, calls `func_1` with the provided arguments, and prints the result. No other variables are affected.
#Overall this is what the function does:The function `func_2` reads the number of test cases `t` from the standard input. For each test case, it reads the number of children `n`, the number of pairs of friends `m`, and the number of excursions `k`. It then reads `m` lines, each containing the indices of a pair of friends and their initial friendship value. The function processes these inputs by calling another function `func_1` and prints the result for each test case. The value of `t` remains unchanged, and no other variables are affected.

