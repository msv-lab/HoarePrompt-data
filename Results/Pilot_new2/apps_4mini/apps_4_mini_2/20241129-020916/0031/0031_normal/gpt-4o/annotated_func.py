#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `b` is 0, `a` is the greatest common divisor (GCD) of the original values of `n` and `k`, and both `n` and `k` remain unchanged.
    return a
    #The program returns the greatest common divisor (GCD) of the original values of n and k
#Overall this is what the function does:The function accepts two integers `a` and `b`, and returns the greatest common divisor (GCD) of `a` and `b`. The function utilizes the Euclidean algorithm to compute the GCD. Since `b` can be reduced to zero, the algorithm will always terminate correctly. The function does not handle input validation, but it assumes that both parameters `a` and `b` are within the expected ranges.

#State of the program right berfore the function call: n and k are integers where 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.
def func_2(n, k):
    MOD = 10 ** 6 + 3
    if (k > 1 << n) :
        print(1, 1)
        return
        #The program returns nothing as there is no value specified to be returned.
    #State of the program after the if block has been executed: *`n` and `k` are integers where 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18; `MOD` is 1000003. The value of `k` is less than or equal to 1 left-shifted by `n` (i.e., k ≤ 2^n).
    total_days = 1 << n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = numerator * (total_days - i) % MOD
        
        denominator = denominator * total_days % MOD
        
    #State of the program after the  for loop has been executed: `n` is an integer where 1 ≤ n ≤ 10^18; `k` is an integer where 2 ≤ k ≤ 10^18; `MOD` is 1000003; `total_days` is equal to \(2^n\); `numerator` is \( (2^n) \times (2^n - 1) \times (2^n - 2) \times \ldots \times (2^n - (k - 1)) \mod 1000003\); `denominator` is \( (2^n)^k \mod 1000003\).
    p_no_shared = numerator
    p_total = denominator
    p_shared = (p_total - p_no_shared + MOD) % MOD
    A = p_shared
    B = p_total
    g = func_1(A, B)
    A //= g
    B //= g
    print(A % MOD, B % MOD)
#Overall this is what the function does:The function accepts two integers `n` and `k`, where `1 ≤ n ≤ 10^18` and `2 ≤ k ≤ 10^18`. It performs calculations based on these parameters but does not return any values. If `k` is greater than `2^n`, it prints `(1, 1)` and exits. Otherwise, it computes the number of possible selections of `k` items from `2^n` items, handling calculations modulo `1000003`, and prints the final results after further calculations. However, the function does not return anything explicitly, and thus its output is solely through printed values, not a return statement.

