#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4; for each test case, n, m, and k are integers where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 · 10^5; each of the next m lines contains three integers a_i, b_i, and f_i where 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and 1 ≤ f_i ≤ 10^9; the sum of n and the sum of m over all test cases do not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
def func():
    MOD = 1000000007
    T = int(input())
    for _ in range(T):
        n, p, k = map(int, input().split())
        
        S = 0
        
        for i in range(p):
            S += int(input().split()[2])
        
        C = n * (n - 1) // 2
        
        num = p * k * k - p * k + 2 * k * C * S
        
        den = 2 * C * C
        
        g = math.gcd(num, den)
        
        num = num // g
        
        den = den // g
        
        den = pow(den, -1, MOD)
        
        ans = num * den % MOD
        
        print(ans)
        
    #State: After the loop executes all iterations, `T` is 0, `n`, `p`, and `k` are the input integers for the last iteration, `S` is the sum of the integer values of the third elements from the `p` input lines for the last iteration, `i` is `p-1`, `C` is `n * (n - 1) // 2` for the last iteration, `den` is the modular multiplicative inverse of `2 * C * C // g` modulo `MOD` for the last iteration, `g` is the GCD of `num` and `2 * C * C` for the last iteration, `num` is `(p * k * k - p * k + 2 * k * C * S) // g` for the last iteration, `ans` is `num * den % MOD` for the last iteration.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads the number of nodes `n`, a parameter `p`, and a condition `k`. It then reads `p` lines of input, each containing three integers, and sums the third integer from each line. Using this sum and other derived values, it calculates a result based on a specific formula involving modular arithmetic and prints the result. The function does not return any value; it only prints the results for each test case. After processing all test cases, the function completes its execution.

