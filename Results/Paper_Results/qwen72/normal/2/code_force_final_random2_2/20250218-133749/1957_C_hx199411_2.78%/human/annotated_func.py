#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 3 × 10^5 and 0 ≤ k ≤ n, representing the size of the chessboard and the number of moves already played, respectively. Each of the next k lines contains two integers r_i and c_i, denoting the i-th move made, where 1 ≤ r_i, c_i ≤ n. The k moves and the implied computer moves are valid, and the sum of n over all test cases does not exceed 3 × 10^5.
def func():
    t = int(input())
    while t:
        t -= 1
        
        n, k = list(map(int, input().split(' ')))
        
        num = 0
        
        for i in range(k):
            c, r = list(map(int, input().split(' ')))
            if c == r:
                num += 1
            else:
                num += 2
        
        m = n - num
        
        if m == 0:
            print(0)
        elif m == 1:
            print(1)
        else:
            dp = [(0) for i in range(m + 1)]
            dp[1] = 1
            dp[2] = 3
            for i in range(3, m + 1):
                dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10 ** 9 + 7)
            print(dp[m])
        
    #State: `t` is 0, `n` is the last integer value provided by the user input, `k` is the last integer value provided by the user input, `i` is `k-1`, `num` is the sum of 1 for each pair `(c, r)` where `c` equals `r`, and 2 for each pair `(c, r)` where `c` does not equal `r`, `m` is `n - num`. If `m` is 0, the program prints 0. If `m` is 1, the program prints 1. If `m` is at least 3, `dp` is a list of length `m + 1` initialized with zeros, where `dp[1]` is 1, `dp[2]` is 3, and for each index `j` from 3 to `m`, `dp[j]` is updated to `(dp[j - 1] + (j - 1) * dp[j - 2] * 2) % (10^9 + 7)`, and the program prints `dp[m]`.
#Overall this is what the function does:The function processes a series of test cases, each defined by a chessboard size `n` and a number of moves `k`. For each test case, it reads `k` pairs of coordinates `(r, c)` representing moves on the chessboard. It calculates a value `num` based on these moves: adding 1 for each move where `r` equals `c`, and 2 otherwise. It then computes `m` as `n - num`. Depending on the value of `m`, the function either prints 0 if `m` is 0, prints 1 if `m` is 1, or computes and prints a dynamic programming result for `m` greater than 1. The dynamic programming result is calculated using a specific recurrence relation and modulo operation. After processing all test cases, the function terminates with `t` set to 0.

