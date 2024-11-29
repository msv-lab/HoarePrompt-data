#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `b` is 0, `a` is the GCD of the original values of `a` and `b`
    return a
    #The program returns the GCD of the original values of 'a' and 'b', where 'b' is 0
#Overall this is what the function does:The function accepts two integers `a` and `b` and returns the GCD of `a` and `b`.

#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.
def func_2(n, k):
    MOD = 10 ** 6 + 3
    if (k > 1 << n) :
        print(1, 1)
        return
        #The program returns (1, 1)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ n ≤ 10^18, `k` is an integer such that 2 ≤ k ≤ 10^18, and `k` is less than or equal to 1 shifted left by `n` (k ≤ 2^n), `MOD` is 1000003.
    total_days = 1 << n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = numerator * (total_days - i) % MOD
        
        denominator = denominator * total_days % MOD
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \( 1 \leq n \leq 10^{18} \); `k` is an integer such that \( 2 \leq k \leq 10^{18} \); `MOD` is \( 1000003 \); `total_days` is equal to \( 2^n \); `numerator` is equal to the product of \( (2^n) \times (2^n - 1) \times \ldots \times (2^n - (k - 1)) \mod 1000003 \); `denominator` is equal to \( (2^n)^k \mod 1000003 \).
    p_no_shared = numerator
    p_total = denominator
    p_shared = (p_total - p_no_shared + MOD) % MOD
    A = p_shared
    B = p_total
    g = func_1(A, B)
    A //= g
    B //= g
    print(A % MOD, B % MOD)
#Overall this is what the function does:The function accepts two integers, `n` and `k`, and returns (1, 1) if `k` is greater than \(2^n\). Otherwise, it computes values based on combinatorial logic involving `n` and `k`, but the final output is still (1, 1) regardless of the computations. Therefore, the function effectively always returns (1, 1).

