#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 3 × 10^5 and 0 ≤ k ≤ n, representing the size of the chessboard and the number of moves already played, respectively. Each of the next k lines contains two integers r_i and c_i, denoting the i-th move made, with 1 ≤ r_i, c_i ≤ n. The k moves and the implied computer moves are valid, and the sum of n over all test cases does not exceed 3 × 10^5.
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
        
    #State: `t` is 0, `n` and `k` are the final inputs provided by the user for the last test case, `num` is the total number of points accumulated based on the equality or inequality of `c` and `r` for all moves in the last test case, `m` is `n - num` for the last test case, and `dp` is a list of length `m + 1` initialized with zeros, where `dp[1]` is 1, `dp[2]` is 3, and `dp[i]` for each `i` from 3 to `m` is updated to `(dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10^9 + 7)` for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each involving a chessboard of size `n` and a series of `k` moves. For each test case, it calculates a score based on the moves: if a move is on the diagonal (`r == c`), it adds 1 to the score; otherwise, it adds 2. It then computes the remaining squares `m` as `n - score`. If `m` is 0, it prints 0. If `m` is 1, it prints 1. Otherwise, it calculates the number of ways to place non-attacking rooks on the remaining squares using dynamic programming and prints the result modulo \(10^9 + 7\). After processing all test cases, the function terminates with `t` set to 0, and the final values of `n`, `k`, `num`, `m`, and `dp` reflect the last test case processed.

