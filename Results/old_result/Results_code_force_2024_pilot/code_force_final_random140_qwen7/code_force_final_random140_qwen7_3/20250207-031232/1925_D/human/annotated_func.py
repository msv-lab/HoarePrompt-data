#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 ⋅ 10^5. Additionally, for each of the m lines describing the friendships, a_i, b_i, and f_i are integers such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9.
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
        
    #State: Output State: The output state after the loop executes all the iterations is `ans`, which is calculated as follows:
    #
    #- `T` is the total number of test cases, and it must be within the range 1 ≤ T ≤ 50000.
    #- For each test case, `n`, `p`, and `k` are input integers.
    #- `S` is the sum of the third elements from the input split by spaces for each iteration from `p` to `2p-1`.
    #- `C` is calculated as `n * (n - 1) // 2`.
    #- `num` is calculated as `(p * k * k - p * k + 2 * k * C * S) // g`, where `g` is the greatest common divisor of `num` and `den`.
    #- `den` is initially `2 * C * C`, but it is then divided by `g` to simplify.
    #- `den` is further simplified by taking its modular multiplicative inverse modulo `MOD` (1000000007).
    #- Finally, `ans` is calculated as `num * den % MOD`.
    #
    #In summary, `ans` will contain the result of the formula applied to all iterations of the loop for each test case, ensuring that the final answer is computed modulo `1000000007`.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes integers \( n \), \( p \), and \( k \). It also processes additional lines of data for each test case, each containing integers \( a_i \), \( b_i \), and \( f_i \). For each test case, the function calculates a value based on the given inputs and arithmetic operations, including the computation of sums, gcd, and modular arithmetic. The final result, \( ans \), is printed for each test case, representing the outcome of the specified formula, adjusted for the given constraints and modulo \( 1000000007 \).

