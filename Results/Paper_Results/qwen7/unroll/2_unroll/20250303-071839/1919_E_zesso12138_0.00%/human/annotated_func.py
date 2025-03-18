#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 5000, and p is a list of n integers where |p[i]| ≤ n and p is sorted in non-decreasing order.
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
        
    #State: Output State: `dp` is a list of length 2 * n + 1 filled with zeros, and `p` is a list of n integers where |p[i]| ≤ n and `p` is sorted in non-decreasing order; `offset` is n.
    final_sum = p[-1] + offset
    return dp[final_sum]
    #The program returns dp[final_sum], where final_sum is p[-1] + n and dp is a list of length 2 * n + 1 filled with zeros.
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer between 1 and 5000 (inclusive), and `p`, a list of `n` integers sorted in non-decreasing order with each element's absolute value not exceeding `n`. It initializes a list `dp` of length `2 * n + 1` with zeros. The function then iteratively updates `dp` based on its previous values, ensuring that each element in `dp` is updated modulo some `MOD`. After completing these updates, the function calculates `final_sum` as the sum of the last element of `p` and `n`, and returns the value at `dp[final_sum]`.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, n is a positive integer such that 1 <= n <= 5000 representing the size of the hidden array a, and p is a list of n integers where |p_i| <= n and p is sorted in non-decreasing order.
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
        
    #State: index is 2 + 2 * t, t is the number of iterations, n is the sum of the integers obtained from data[index:index + n] for each iteration, p is a list of integers obtained from data[index:index + n] for each iteration, results is a list containing the results of calling func_1(n, p) for each iteration.
    for res in results:
        print(res)
        
    #State: index is 2 + 2 * t, t is the number of iterations, n is the sum of the integers obtained from data[index:index + n] for each iteration, p is a list of integers obtained from data[index:index + n] for each iteration, results is a list containing the results of calling func_1(n, p) for each iteration, no change in the loop, only printing the results.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the size of the hidden array `n` and a list of `n` integers `p`. It then calls another function `func_1(n, p)` to compute a result for each test case. Finally, it prints the results of these computations for all test cases.

