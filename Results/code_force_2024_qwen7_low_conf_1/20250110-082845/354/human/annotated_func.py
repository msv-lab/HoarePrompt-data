#State of the program right berfore the function call: c1, c2, c3, and c4 are non-negative integers such that 0 <= c1, c2, c3, c4 <= 10^6.
def func_1(c1, c2, c3, c4):
    MOD = 998244353
    dp = [[(0) for _ in range(4)] for _ in range(max(c1, c2, c3, c4) + 1)]
    dp[0][0] = 1
    for i in range(1, max(c1, c2, c3, c4) + 1):
        if i <= c1:
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]) % MOD
        
        if i <= c2:
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][3]) % MOD
        
        if i <= c3:
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3]) % MOD
        
        if i <= c4:
            dp[i][3] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
        
    #State of the program after the  for loop has been executed: `c1`, `c2`, `c3`, `c4` are non-negative integers such that \(0 \leq c1, c2, c3, c4 \leq 10^6\), `MOD` is 998244353, `dp` is a 2D list of size \((\max(c1, c2, c3, c4) + 1) \times 4\), with each element updated according to the loop rules, and `i` is \(\max(c1, c2, c3, c4) + 1\).
    total_ways = sum(dp[max(c1, c2, c3, c4)]) % MOD
    return total_ways
    #`The program returns total_ways which is the sum of dp[i] modulo 998244353 where i is max(c1, c2, c3, c4) + 1`
#Overall this is what the function does:- If any of `c1`, `c2`, `c3`, or `c4` is zero, the corresponding entries in the `dp` table will not be updated because the conditions `if i <= c1`, etc., will not be met. However, since the initial value `dp[0][0]` is set to 1, the sum of the last row will still correctly represent the total number of ways, as long as at least one of `c1`, `c2`, `c3`, or `c4` is non-zero.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and for each test case, c1, c2, c3, and c4 are non-negative integers representing the count of elements of each type, respectively. Additionally, the sum of c1, c2, c3, and c4 for each test case does not exceed 4 * 10^6.
def func_2():
    MOD = 998244353
    t = int(input())
    results = []
    for _ in range(t):
        c1, c2, c3, c4 = map(int, input().split())
        
        result = func_1(c1, c2, c3, c4)
        
        results.append(result)
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer, `c1`, `c2`, `c3`, and `c4` are integers obtained from the input for each iteration, `result` is the return value of `func_1(c1, c2, c3, c4)` for each iteration, `results` is a list containing `t` elements, each being the `result` of the respective iteration.
    for result in results:
        print(result)
        
    #State of the program after the  for loop has been executed: `t` is a non-negative integer, `c1`, `c2`, `c3`, and `c4` are integers obtained from the input for each iteration, `result` is the return value of `func_1(c1, c2, c3, c4)` for the last iteration, `results` is a list containing `t` elements, each being the `result` of the respective iteration, and the contents of `results` are printed.
#Overall this is what the function does:The function `func_2` processes multiple test cases, where each test case consists of four non-negative integers `c1`, `c2`, `c3`, and `c4`. For each test case, it calls the function `func_1(c1, c2, c3, c4)` to compute a result, which is then stored in a list `results`. After processing all test cases, it prints each result from the `results` list. The function accepts a single positive integer `t` representing the number of test cases and returns no explicit value (though it modifies the `results` list internally). The state of the program after the function concludes includes the `results` list containing the computed results for each test case.

