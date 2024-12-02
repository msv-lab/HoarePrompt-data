#State of the program right berfore the function call: **Input**: The input consists of two integers, \(n\) and \(k\) (1 ≤ \(n\) ≤ \(10^{18}\), 2 ≤ \(k\) ≤ \(10^{18}\), representing the number of days in a year (2^n) and the number of people interviewed (k) by ZS the Coder.

**Output**: The output should be two integers, A and B, representing the irreducible fraction A/B where A and B are coprime and must be printed modulo 10^6 + 3.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: The loop will execute multiple times until `b` becomes 0. After the loop finishes, `a` will store the GCD of the original values of `a` and `b`, and `b` will be 0.
    return a
    #The program returns the GCD of the original values of `a` and `b`, where `a` stores the GCD and `b` becomes 0 after the loop finishes.
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `b`, both integers. It calculates the greatest common divisor (GCD) of the original values of `a` and `b` using the Euclidean algorithm. The resulting GCD is stored in `a`, and `b` becomes 0 after the loop finishes. The program returns the GCD of the original values of `a` and `b`, which is stored in `a` and must be printed modulo 10^6 + 3.

#State of the program right berfore the function call: **Precondition**: **n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.**
def func_2(n, k):
    MOD = 10 ** 6 + 3
    if (k > 1 << n) :
        print(1, 1)
        return
        #The program returns the current value of 'k' after shifting it left by 'n' bits, where 'k' is an integer such that 2 ≤ k ≤ 10^18 and 'n' is an integer such that 1 ≤ n ≤ 10^18
    #State of the program after the if block has been executed: *`MOD` is assigned the value 1000003. `n` is an integer such that 1 ≤ n ≤ 10^18. `k` is an integer such that 2 ≤ k ≤ 10^18. `k` is less than or equal to 1 shifted left by `n`.
    total_days = 1 << n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = numerator * (total_days - i) % MOD
        
        denominator = denominator * total_days % MOD
        
    #State of the program after the  for loop has been executed: Output State: `MOD` is assigned the value 1000003, `n` is an integer such that 1 ≤ n ≤ 10^18, `k` is an integer such that k is greater than or equal to 1, `total_days` is equal to 2 to the power of n, `numerator` is assigned the value calculated by `numerator * (total_days - k) % MOD`, `denominator` is assigned the value `total_days^k % MOD`
    p_no_shared = numerator
    p_total = denominator
    p_shared = (p_total - p_no_shared + MOD) % MOD
    A = p_shared
    B = p_total
    g = func_1(A, B)
    A //= g
    B //= g
    print(A % MOD, B % MOD)
#Overall this is what the function does:The function `func_2` accepts two integer parameters `n` and `k`, where `n` should be in the range 1 to 10^18 and `k` should be in the range 2 to 10^18. The function then calculates the value of `k` after left shifting it by `n` bits and prints the result. Additionally, it performs a series of calculations involving modulo operations and another function `func_1` to compute and print specific values.

