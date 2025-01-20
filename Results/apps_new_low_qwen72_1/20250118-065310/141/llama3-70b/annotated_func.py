#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 80 and n ≤ m ≤ 100,000. There are n lines following the first line, each containing two integers x_i and s_i where 1 ≤ x_i ≤ m and 0 ≤ s_i ≤ m, and all x_i are distinct.
def func():
    n, m = map(int, input().split())

antennas = []
    for _ in range(n):
        x, s = map(int, input().split())
        
        antennas.append((x, s))
        
    #State of the program after the  for loop has been executed: n is an integer such that 1 ≤ n ≤ 80, m is an integer such that n ≤ m ≤ 100,000, antennas is a list containing n tuples (x1, s1), (x2, s2), ..., (xn, sn) where x1, s1, x2, s2, ..., xn, sn are integers provided by the input.
    antennas.sort()

dp = [float('inf')] * (m + 1)

dp[0] = 0
    for (x, s) in antennas:
        for i in range(m, x - s - 1, -1):
            dp[i] = min(dp[i], dp[max(0, i - x - s)] + (i - x + s))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 80\), `m` is an integer such that \(n \leq m \leq 100,000\), `antennas` is a sorted list of `n` tuples \((x_1, s_1), (x_2, s_2), \ldots, (x_n, s_n)\) where \(x_1, s_1, x_2, s_2, \ldots, x_n, s_n\) are integers, `dp` is a list of length \(m + 1\) where `dp[0]` is 0, and for each index `i` in the range \([0, m]\), `dp[i]` is updated to the minimum value computed by the loop over all antennas, and all other elements are no longer `float('inf')` but reflect the optimal values based on the dynamic programming updates. The loop iterates over each antenna in `antennas`, and for each antenna, it updates the `dp` array from `m` down to `x - s - 1`, ensuring that the minimum cost is calculated for each position. Variables `n`, `m`, and `antennas` remain constant throughout the loop.
    print(dp[m])
#Overall this is what the function does:The function `func` reads input data consisting of integers `n` and `m` (where \(1 \leq n \leq 80\) and \(n \leq m \leq 100,000\)), followed by `n` pairs of integers \((x_i, s_i)\) (where \(1 \leq x_i \leq m\) and \(0 \leq s_i \leq m\), and all \(x_i\) are distinct). It then processes this data to compute the minimum cost required to cover the entire range from 0 to \(m\) using the given antennas. The function sorts the list of antennas based on their positions \(x_i\) and uses dynamic programming to find the minimum cost. Finally, it prints the minimum cost to cover the range up to \(m\). The function does not return any value; it only prints the result. If the input does not meet the specified constraints, the behavior of the function is undefined.

