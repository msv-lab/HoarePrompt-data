#State of the program right berfore the function call: n is an integer representing the number of children, m is an integer representing the number of pairs of friends, k is an integer representing the number of excursions, and friendships is a list of tuples, where each tuple contains three integers (a, b, f) representing the indices of the pair of children who are friends and their friendship value respectively. All values are such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n*(n-1)/2), 1 ≤ k ≤ 2*10^5, and 1 ≤ f ≤ 10^9. Additionally, the sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2*10^5. The constant MOD is set to 10^9 + 7.
def func_1(n, m, k, friendships):
    result = 0
    for i in range(m):
        a, b, f = friendships[i]
        
        result += f * (k * (k + 1) // 2) % MOD
        
    #State: Output State: `result` is `m * f * (k * (k + 1) // 2) % MOD`, `n` is an integer representing the number of children, `m` is an integer representing the number of pairs of friends, `k` is an integer representing the number of excursions, `friendships` is a list of tuples with at least one tuple, `i` is `m`, `a` is not defined since the loop has completed, `b` is not defined since the loop has completed, `f` is not defined since the loop has completed.
    #
    #Explanation: After the loop completes all its iterations, the variable `result` accumulates the sum of `f * (k * (k + 1) // 2) % MOD` for each of the `m` iterations. Therefore, the final value of `result` is `m * f * (k * (k + 1) // 2) % MOD`. The other variables (`n`, `m`, `k`, `friendships`, `i`, `a`, `b`, and `f`) retain their post-loop iteration states, which in this case, means `i` would be equal to `m` since the loop has finished executing all `m` iterations.
    return result % MOD
    #The program returns the value of `result` which is `m * f * (k * (k + 1) // 2) % MOD`
#Overall this is what the function does:The function accepts four parameters: `n` (number of children), `m` (number of pairs of friends), `k` (number of excursions), and `friendships` (a list of tuples containing friend indices and their values). It calculates and returns the value of `result` which is `m * f * (k * (k + 1) // 2) % MOD`, where `f` is the friendship value from the `friendships` list and `MOD` is set to \(10^9 + 7\).

#State of the program right berfore the function call: t is an integer representing the number of test cases, n is an integer representing the number of children, m is an integer representing the number of pairs of friends, k is an integer representing the number of excursions, and friendships is a list of lists where each inner list contains three integers [a_i, b_i, f_i] representing the indices of the pair of children who are friends and their friendship value respectively.
def func_2():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        friendships = [list(map(int, input().split())) for _ in range(m)]
        
        result = func_1(n, m, k, friendships)
        
        print(result)
        
    #State: Output State: `t` must be greater than or equal to the total number of times the loop has executed, `n` is the last input integer received, `m` is the last input integer received, `k` is the last input integer received, `friendships` is a list of `m` lists, each containing two integers (the last set of friendships entered), `result` is the cumulative return value of `func_1(n, m, k, friendships)` for each iteration of the loop.
    #
    #In simpler terms, after the loop has executed all its iterations, `t` will be the final value it was set to, `n`, `m`, and `k` will hold the values from the last iteration, `friendships` will contain the last set of friendships entered, and `result` will be the combined result of applying `func_1` in each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves a specified number of children (`n`), pairs of friends (`m`), excursions (`k`), and their friendships represented as a list of lists. For each test case, it calls `func_1(n, m, k, friendships)` to compute a result, then prints the cumulative result after processing all test cases. The final output includes the results of all test cases.

