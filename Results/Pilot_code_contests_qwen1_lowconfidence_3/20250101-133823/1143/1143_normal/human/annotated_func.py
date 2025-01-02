#State of the program right berfore the function call: n is an integer representing the number of stones, k is an integer such that 1 ≤ k ≤ 100, and arr is a list of integers representing the heights of the stones (h_1, h_2, ..., h_n) where 1 ≤ h_i ≤ 10^4.
def func_1():
    n, k = read()
    arr = read()
    dp = [-1] * n
    dp[0] = 0
    for i in range(n):
        for j in range(1, k + 1):
            if i - j > -1:
                tem = dp[i - j] + abs(arr[i - j] - arr[i])
                if dp[i] == -1:
                    dp[i] = tem
                elif dp[i] > tem:
                    dp[i] = tem
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `k` is an integer such that 1 ≤ k ≤ 100 and \(k \leq n\), `arr` is a list updated to the value returned by `read()`, `dp` is a list of length `n` filled with `-1` except `dp[0]` which is `0`. After all iterations of the loop, for each index `i` from `0` to `n-1`, `dp[i]` is the minimum cost to reach index `i` starting from index `0`, where the cost is defined as the sum of the absolute differences between consecutive elements in `arr` up to the current index `i`. If `i - j` is not greater than -1, the value of `dp[i]` remains unchanged. If the loop does not execute at all, `dp` remains a list of length `n` filled with `-1` (except `dp[0]` which is `0`).
    print(dp[-1])
#Overall this is what the function does:The function `func_1` accepts three parameters: `n` (an integer representing the number of stones), `k` (an integer such that 1 ≤ k ≤ 100), and `arr` (a list of integers representing the heights of the stones). It calculates the minimum cost to jump from the first stone to the last stone, where each jump can be up to `k` stones away. The cost of a jump is the absolute difference in height between the two stones. The function initializes a dynamic programming array `dp` where `dp[i]` represents the minimum cost to reach the `i-th` stone from the first stone. The function iterates through the stones, updating `dp[i]` with the minimum cost to reach each stone. Finally, the function prints the minimum cost to reach the last stone (`dp[-1]`).

#State of the program right berfore the function call: l is a list of zeros with a length of 10^7.
def func_2():
    l = [0] * 10 ** 7
#Overall this is what the function does:The function `func_2()` takes a list `l` as input, which is initially a list of one million zeros. The function does not modify the list `l` in any way and simply returns the same list `l`. There are no edge cases or missing functionalities since the list remains unchanged throughout the function execution.

#State of the program right berfore the function call: This function does not use any of the variables from the main problem description. Instead, it initializes a list `l` of zeros with a length of 10^7. This suggests that there might be another function or part of the solution that uses this list to store intermediate results or costs, but no such usage is shown here.
def func_3():
    l = [(0) for i in range(10 ** 7)]
#Overall this is what the function does:This function initializes a list `l` containing \(10^7\) elements, each set to zero. There are no inputs accepted by the function, and it does not return anything. The function does not perform any additional operations on the list beyond initialization. Therefore, after the function concludes, the state of the program includes a global list `l` with \(10^7\) elements, all initialized to zero. No other variables or states are affected by this function.

