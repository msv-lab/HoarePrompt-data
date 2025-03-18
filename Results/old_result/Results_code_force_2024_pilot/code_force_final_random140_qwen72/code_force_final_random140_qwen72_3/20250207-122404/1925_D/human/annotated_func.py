#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 5 · 10^4, representing the number of test cases. For each test case, n, m, and k are integers where 2 ≤ n ≤ 10^5, 0 ≤ m ≤ min(10^5, n(n-1)/2), and 1 ≤ k ≤ 2 · 10^5, representing the number of children, pairs of friends, and excursions, respectively. Each of the next m lines contains three integers a_i, b_i, and f_i where 1 ≤ a_i, b_i ≤ n, a_i ≠ b_i, and 1 ≤ f_i ≤ 10^9, representing the indices of the pair of children who are friends and their initial friendship value. The sum of n and m over all test cases does not exceed 10^5, and the sum of k over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations of the loop, `T` is 0, `ans` has been printed for each test case, and the values of `n`, `p`, `k`, `S`, `i`, `C`, `num`, `den`, and `g` are recalculated for each test case based on the input provided for that test case.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by the number of children (`n`), pairs of friends (`p`), and excursions (`k`). For each test case, it reads the friendship values for the first `p` pairs of friends, calculates a specific mathematical expression involving these values, and prints the result modulo 1000000007. The function does not return any value; instead, it outputs the result for each test case directly. After processing all test cases, the function completes, and the state of the program reflects that all test cases have been processed and their results printed.

