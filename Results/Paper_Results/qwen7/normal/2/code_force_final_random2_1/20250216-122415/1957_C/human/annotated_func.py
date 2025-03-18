#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 3 ⋅ 10^5 and 0 ≤ k ≤ n. The coordinates (r_i, c_i) for each move you made are integers such that 1 ≤ r_i, c_i ≤ n.
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
        
    #State: `t` is 0, `n` is an integer, `k` is an integer, `num` is an integer, `i` is 0, `c` is the last integer read from input, `r` is the last integer read from input, `m` is `n - num`, and `dp` is a list of length `m + 1` where each element `dp[i]` (for i from 1 to m) is computed as `(dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10^9 + 7)` for all i from 3 to m.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers \( n \) and \( k \), followed by \( k \) pairs of integers representing coordinates \( (r_i, c_i) \). It calculates the number of coordinates where \( c_i \) equals \( r_i \) and adds 2 for all other coordinates. It then computes \( m \) as \( n - \text{num} \), where \( \text{num} \) is the total count calculated earlier. Based on the value of \( m \), it either prints 0, 1, or a specific value derived using dynamic programming, modulo \( 10^9 + 7 \).

