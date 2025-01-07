#State of the program right berfore the function call: a and b are integers such that 1 ≤ a ≤ 10^18 and 2 ≤ b ≤ 10^18.**
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `a` holds the GCD of the original values of `a` and `b`, `b` is 0
    return a
    #The program returns the GCD of the original values of `a` and 0
#Overall this is what the function does:The function func_1 accepts two integer parameters `a` and `b`, calculates the Greatest Common Divisor (GCD) of their original values, and returns the GCD. The function implements the Euclidean algorithm to compute the GCD. In case where `b` is initially 0, it returns the original value of `a` as the GCD. The function handles edge cases where `a` and `b` are within specified ranges.

#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.**
def func_2(n, k):
    MOD = 10 ** 6 + 3
    if (k > 1 << n) :
        print(1, 1)
        return
        #The program does not return any specific value, as no calculations or operations are performed.
    #State of the program after the if block has been executed: *n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18, MOD is 1000003. k is less than or equal to 1 shifted left by n
    total_days = 1 << n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = numerator * (total_days - i) % MOD
        
        denominator = denominator * total_days % MOD
        
    #State of the program after the  for loop has been executed: Output State: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18, MOD is 1000003, k is at least 2, `total_days` is equal to 2^n, `numerator` is equal to the factorial of 2^n modulo MOD, `denominator` is equal to the factorial of k modulo MOD.
    p_no_shared = numerator
    p_total = denominator
    p_shared = (p_total - p_no_shared + MOD) % MOD
    A = p_shared
    B = p_total
    g = func_1(A, B)
    A //= g
    B //= g
    print(A % MOD, B % MOD)
#Overall this is what the function does:The function `func_2` accepts two integer parameters `n` and `k` within the specified constraints. If `k` is greater than 1 shifted left by `n`, the function prints '1 1' and exits. Otherwise, it calculates values for `numerator`, `denominator`, `p_no_shared`, `p_total`, `p_shared`, `A`, `B`, and `g` based on the input parameters. The calculated values are then used to print `(A % MOD, B % MOD)`. In case the conditions specified in the annotations are not met, the functionality may deviate from what is described.

