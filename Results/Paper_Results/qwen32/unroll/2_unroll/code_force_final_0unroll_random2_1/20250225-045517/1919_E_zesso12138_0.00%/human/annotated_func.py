#State of the program right berfore the function call: n is a positive integer representing the size of the hidden array a, and p is a list of integers of length n representing the sorted prefix sums of array a, where each element in p satisfies -n <= p_i <= n.
def func_1(n, p):
    dp = [0] * (2 * n + 1)
    offset = n
    dp[offset] = 1
    for i in range(1, n + 1):
        new_dp = [0] * (2 * n + 1)
        
        for j in range(2 * n + 1):
            if dp[j] > 0:
                if j + 1 <= 2 * n:
                    new_dp[j + 1] = (new_dp[j + 1] + dp[j]) % MOD
                if j - 1 >= 0:
                    new_dp[j - 1] = (new_dp[j - 1] + dp[j]) % MOD
        
        dp = new_dp
        
    #State: `n` is a positive integer, `p` is a list of integers of length `n`, `dp` is a list of integers of length `2 * n + 1` representing the number of ways to reach each possible sum after `n` steps, `offset` is `n`.
    final_sum = p[-1] + offset
    return dp[final_sum]
    #The program returns the number of ways to reach the sum `p[-1] + n` after `n` steps, as represented by `dp[p[-1] + n]`.
#Overall this is what the function does:The function calculates and returns the number of ways to reach the sum `p[-1] + n` after `n` steps, using dynamic programming. It accepts two parameters: `n`, a positive integer representing the size of the hidden array `a`, and `p`, a list of integers of length `n` representing the sorted prefix sums of array `a`, where each element in `p` satisfies -n <= p_i <= n.

#State of the program right berfore the function call: n is a positive integer representing the size of the hidden array a, and p is a list of integers of length n representing the sorted prefix sums of array a.
def func_2():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        p = list(map(int, data[index:index + n]))
        
        index += n
        
        result = func_1(n, p)
        
        results.append(result)
        
    #State: `n` is the size of the array `a` from the last iteration, `p` is the list of prefix sums from the last iteration, `index` is the position after the last prefix sums in `data`, `t` is the number of iterations, and `results` is a list of results from each iteration of `func_1(n, p)`.
    for res in results:
        print(res)
        
    #State: `n` is the size of the array `a` from the last iteration, `p` is the list of prefix sums from the last iteration, `index` is the position after the last prefix sums in `data`, `t` is the number of iterations, and `results` is a list of results from each iteration of `func_1(n, p)`. The contents of `results` have been printed.
#Overall this is what the function does:The function `func_2` reads input from standard input, processes multiple test cases, and for each test case, it calculates and prints a hidden array `a` based on the given sorted prefix sums `p`.

