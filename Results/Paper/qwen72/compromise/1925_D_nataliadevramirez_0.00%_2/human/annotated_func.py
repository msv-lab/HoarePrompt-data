#State of the program right berfore the function call: n is an integer representing the number of children, m is an integer representing the number of friendship pairs, k is an integer representing the number of excursions, and friendships is a list of tuples where each tuple contains three integers (a, b, f) representing the indices of two children who are friends and their initial friendship value. The values of n, m, and k are such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 * 10^5. Each a and b in the tuples satisfy 1 ≤ a, b ≤ n and a ≠ b, and each f satisfies 1 ≤ f ≤ 10^9.
def func_1(n, m, k, friendships):
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: `n` remains unchanged, `m` remains unchanged, `k` remains unchanged, `friendships` remains unchanged, `result` is the sum of the products of each friendship value `f` in `friendships` multiplied by the value of `k * (k + 1) // 2`, modulo `MOD`.
    return result % MOD
    #The program returns the value of `result % MOD`, where `result` is the sum of the products of each friendship value `f` in `friendships` multiplied by the value of `k * (k + 1) // 2`, modulo `MOD`.
#Overall this is what the function does:The function `func_1` accepts four parameters: `n` (the number of children), `m` (the number of friendship pairs), `k` (the number of excursions), and `friendships` (a list of tuples representing the friendship pairs and their initial values). It calculates the sum of the products of each friendship value `f` in `friendships` multiplied by the value of `k * (k + 1) // 2`, and returns this sum modulo `MOD`. The parameters `n`, `m`, `k`, and `friendships` remain unchanged after the function call.

#State of the program right berfore the function call: No variables are passed to the function `func_2`. The function reads input from the standard input, where the first line contains an integer t (1 ≤ t ≤ 5 · 10^4) representing the number of test cases. For each test case, the first line contains three integers n (2 ≤ n ≤ 10^5), m (0 ≤ m ≤ min(10^5, n(n-1)/2)), and k (1 ≤ k ≤ 2 · 10^5). The next m lines each contain three integers a_i, b_i, and f_i (1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, 1 ≤ f_i ≤ 10^9) representing the indices of the pair of children who are friends and their initial friendship value.
def func_2():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: The value of `t` remains unchanged, and no other variables are affected.
#Overall this is what the function does:The function `func_2` reads multiple test cases from standard input, processes each test case by calling another function `func_1` with the test case data, and prints the result of `func_1` for each test case. The function does not modify any external variables or state outside of its scope, and the value of `t` (the number of test cases) remains unchanged throughout the function's execution.

