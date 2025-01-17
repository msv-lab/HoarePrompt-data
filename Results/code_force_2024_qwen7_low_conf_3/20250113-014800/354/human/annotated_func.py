#State of the program right berfore the function call: c1, c2, c3, c4 are non-negative integers such that 0 <= c1, c2, c3, c4 <= 10^6 and the sum of the elements in each test case does not exceed 4 * 10^6.
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
        
    #State of the program after the  for loop has been executed: Output State: **`i` is equal to `max(c1, c2, c3, c4) + 1`, `dp[max(c1, c2, c3, c4) + 1][0]` is \(((dp[max(c1, c2, c3, c4)][1] + dp[max(c1, c2, c3, c4)][2] + dp[max(c1, c2, c3, c4)][3]) \% MOD\), `dp[max(c1, c2, c3, c4) + 1][1]` is \(((dp[max(c1, c2, c3, c4)][0] + dp[max(c1, c2, c3, c4)][2] + dp[max(c1, c2, c3, c4)][3]) \% MOD\), `dp[max(c1, c2, c3, c4) + 1][2]` is \(((dp[max(c1, c2, c3, c4)][0] + dp[max(c1, c2, c3, c4)][1] + dp[max(c1, c2, c3, c4)][3]) \% MOD\), `dp[max(c1, c2, c3, c4) + 1][3]` is \(((dp[max(c1, c2, c3, c4)][0] + dp[max(c1, c2, c3, c4)][1] + dp[max(c1, c2, c3, c4)][2]) \% MOD\), and all other `dp[i][j]` where `i > max(c1, c2, c3, c4)` and `0 ≤ j ≤ 3` are equal to \(((dp[0][0] + dp[0][2] + dp[0][3]) \% MOD\).
    #
    #Explanation:
    #- The loop iterates from `i = 1` to `i = max(c1, c2, c3, c4)`.
    #- For each iteration, the loop updates the `dp` table based on the conditions `i <= c1`, `i <= c2`, `i <= c3`, and `i <= c4`.
    #- After the loop completes, `i` will be equal to `max(c1, c2, c3, c4) + 1`.
    #- The values of `dp[i][0]`, `dp[i][1]`, `dp[i][2]`, and `dp[i][3]` will be the cumulative sums computed during the loop, modulo `MOD`.
    #- All other `dp[i][j]` where `i > max(c1, c2, c3, c4)` will be reset to \(((dp[0][0] + dp[0][2] + dp[0][3]) \% MOD\), as no further updates are made beyond `i = max(c1, c2, c3, c4)`.
    total_ways = sum(dp[max(c1, c2, c3, c4)]) % MOD
    return total_ways
    #The program returns total_ways which is the sum of dp[max(c1, c2, c3, c4)][0], dp[max(c1, c2, c3, c4)][1], dp[max(c1, c2, c3, c4)][2], and dp[max(c1, c2, c3, c4)][3], modulo MOD.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `c1`, `c2`, `c3`, and `c4`. It constructs a dynamic programming table `dp` to compute the number of ways to achieve a certain state based on the given constraints. The table `dp` is initialized such that `dp[0][0] = 1`, indicating one way to achieve a state with zero items using zero counts. The function then iterates through possible values up to `max(c1, c2, c3, c4)` and updates the table according to specific conditions. After the loop, the function calculates the sum of the last row of the `dp` table (`dp[max(c1, c2, c3, c4)]`) and returns this sum modulo `998244353`. The function handles edge cases where some `ci` values are zero, ensuring that the corresponding entries in the `dp` table are correctly updated based on the remaining `ci` values.

#State of the program right berfore the function call: c1, c2, c3, and c4 are non-negative integers representing the number of elements of each type, where 0 <= c1, c2, c3, c4 <= 10^6.
def func_2():
    MOD = 998244353
    t = int(input())
    results = []
    for _ in range(t):
        c1, c2, c3, c4 = map(int, input().split())
        
        result = func_1(c1, c2, c3, c4)
        
        results.append(result)
        
    #State of the program after the  for loop has been executed: `c1` is an input integer, `c2` is an input integer, `c3` is an input integer, `c4` is an input integer, `MOD` is 998244353, `t` is 0, `results` is a list containing the return values of `func_1(c1, c2, c3, c4)` executed `t` times.
    for result in results:
        print(result)
        
    #State of the program after the  for loop has been executed: `c1` is an input integer, `c2` is an input integer, `c3` is an input integer, `c4` is an input integer, `MOD` is 998244353, `t` is 1, `results` is a list containing the return values of `func_1(c1, c2, c3, c4)` executed `t` times.
#Overall this is what the function does:The function `func_2` reads multiple sets of four non-negative integers (c1, c2, c3, c4) from standard input, calls another function `func_1` with these integers, collects the results in a list, and prints each result. The function does not accept any parameters and does not return a value. The final state of the program includes the list of results after processing all inputs, the modulus constant `MOD` set to 998244353, and the variable `t` set to the number of input sets processed. Potential edge cases include when `t` is 0, in which case no results are collected or printed. Additionally, the function assumes valid integer inputs within the specified range; handling of invalid inputs such as non-integer or out-of-range values is not addressed in the provided code.

