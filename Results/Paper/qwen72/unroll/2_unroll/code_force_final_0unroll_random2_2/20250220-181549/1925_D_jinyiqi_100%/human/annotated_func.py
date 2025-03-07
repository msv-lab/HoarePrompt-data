#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5 * 10^4; for each test case, n, m, and k are integers where 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), and 1 <= k <= 2 * 10^5; a_i, b_i, and f_i are integers for each of the m lines, where a_i ≠ b_i, 1 <= a_i, b_i <= n, and 1 <= f_i <= 10^9; the sum of n and the sum of m over all test cases do not exceed 10^5, and the sum of k over all test cases does not exceed 2 * 10^5.
def func():
    t = int(input())
    M = 10 ** 9 + 7
    for i in range(t):
        n, m, k = map(int, input().split())
        
        sum_f = 0
        
        for j in range(m):
            a, b, f = map(int, input().split())
            sum_f += f
        
        cn2 = n * (n - 1) // 2
        
        p = 2 * k * cn2 * sum_f + m * k * (k - 1)
        
        q = 2 * cn2 ** 2
        
        gcd = math.gcd(p, q)
        
        p = p // gcd
        
        q = q // gcd
        
        print(int(p * pow(q, -1, M) % M))
        
    #State: The loop iterates `t` times, and for each iteration, it reads `n`, `m`, and `k` from the input, then reads `m` lines of input for `a_i`, `b_i`, and `f_i`. It calculates `p` and `q` based on these inputs, simplifies the fraction `p/q` using the greatest common divisor, and prints the result of `(p * pow(q, -1, M)) % M`. After all iterations, the values of `t`, `M`, and the input constraints remain unchanged.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer such that 1 <= t <= 5 * 10^4. For each test case, it reads integers `n`, `m`, and `k` where 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), and 1 <= k <= 2 * 10^5. It then reads `m` lines of input, each containing three integers `a_i`, `b_i`, and `f_i` where 1 <= a_i, b_i <= n, a_i ≠ b_i, and 1 <= f_i <= 10^9. The function calculates a result based on these inputs and prints it. The result is the modular inverse of a fraction `(p/q) % M`, where `M = 10^9 + 7`, and `p` and `q` are derived from the inputs. After processing all test cases, the function does not return any value but prints the results for each test case. The values of `t`, `M`, and the input constraints remain unchanged.

