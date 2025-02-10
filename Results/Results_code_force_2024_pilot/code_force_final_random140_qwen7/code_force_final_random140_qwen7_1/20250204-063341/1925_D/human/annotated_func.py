#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5⋅10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2⋅10^5. Additionally, a_i, b_i, and f_i are integers such that a_i ≠ b_i, 1 ≤ a_i, b_i ≤ n, and 1 ≤ f_i ≤ 10^9. All pairs of friends are distinct, and the sum of n and the sum of m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The output state after the loop executes all the iterations is determined by the final values of the variables `num`, `den`, and `ans` after processing all inputs. Here's the description in natural language:
    #
    #- `num` is calculated as \( p \times k \times k - p \times k + 2 \times k \times C \times S \), where \( C = \frac{n \times (n - 1)}{2} \) and \( S \) is the sum of the third elements from each of the `p` input lists.
    #- `den` is calculated as \( 2 \times C \times C \).
    #- `g` is the greatest common divisor (GCD) of `num` and `den`.
    #- `num` is then divided by `g` to simplify it.
    #- `den` is the modular multiplicative inverse of `den` modulo `1000000007` (denoted as `pow(den, -1, MOD)`).
    #- Finally, `ans` is computed as \( num \times den \mod 1000000007 \).
    #
    #This process is repeated for each of the `T` test cases, and the final value of `ans` for each case is printed.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes integers \( T \), \( n \), \( p \), and \( k \), along with additional integers \( a_i \), \( b_i \), and \( f_i \). For each test case, it calculates a value based on the given inputs and prints the result. Specifically, it computes a simplified fraction \( \frac{\text{num}}{\text{den}} \) modulo \( 1000000007 \), where \( \text{num} \) and \( \text{den} \) are derived from the input values, and then prints the numerator of the simplified fraction.

