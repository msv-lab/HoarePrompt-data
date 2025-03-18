#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 \cdot 10^5 and 0 ≤ k ≤ n. Each of the k moves is represented by a pair of integers (r_i, c_i) such that 1 ≤ r_i, c_i ≤ n, and all moves are valid, meaning no two rooks attack each other.
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
            print(1)
        elif m == 1:
            print(1)
        else:
            dp = [(0) for i in range(m + 1)]
            dp[1] = 1
            dp[2] = 3
            for i in range(3, m + 1):
                dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10 ** 9 + 7)
            print(dp[m])
        
    #State: The loop will have executed `t` times, and for each execution, the value of `m` is calculated and the corresponding value in the `dp` array is printed. The final value of `t` will be 0, and all other variables (`n`, `k`, `num`, `dp`, `m`, `c`, `r`, `i`) will be in their final states after the last iteration of the loop.
#Overall this is what the function does:The function reads multiple test cases, each defined by a chessboard size `n` and a number of moves `k`. For each test case, it processes `k` moves, each represented by a pair of integers `(r_i, c_i)`, and calculates the number of ways to place rooks on the chessboard such that no two rooks attack each other, given the moves. The function prints the result for each test case, which is the number of valid configurations modulo \(10^9 + 7\). After processing all test cases, the function terminates with `t` set to 0 and all other variables in their final states.

