#State of the program right berfore the function call: n and k are integers where 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `b` is 0, `a` is the GCD of the original values of `n` and `k`.
    return a
    #The program returns the GCD of the original values of `n` and `k`
#Overall this is what the function does:The function accepts two integer parameters `a` and `b` and returns the greatest common divisor (GCD) of the original values of `a` and `b` using the Euclidean algorithm. The function correctly handles cases where either `a` or `b` is zero, returning the non-zero value as the GCD, or zero if both are zero. The input values are expected to be within the ranges provided (1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18).

#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.
def func_2(n, k):
    MOD = 10 ** 6 + 3
    if (k > 1 << n) :
        print(1, 1)
        return
        #The program returns None, as there is no value being returned from the function.
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ n ≤ 10^18, `k` is an integer such that 2 ≤ k ≤ 10^18, `MOD` is 1000003, and `k` is less than or equal to 1 << n.
    total_days = 1 << n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = numerator * (total_days - i) % MOD
        
        denominator = denominator * total_days % MOD
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 10^18, `k` is an integer such that 2 ≤ k ≤ 10^18, `k` is less than or equal to 1 << n, `MOD` is 1000003, `total_days` is equal to 2^n, `numerator` is equal to the product of ((2^n) - i) for i from 0 to k-1 modulo 1000003, `denominator` is equal to (total_days^k) % 1000003.
    p_no_shared = numerator
    p_total = denominator
    p_shared = (p_total - p_no_shared + MOD) % MOD
    A = p_shared
    B = p_total
    g = func_1(A, B)
    A //= g
    B //= g
    print(A % MOD, B % MOD)
#Overall this is what the function does:The function accepts two integers `n` and `k`, where `1 ≤ n ≤ 10^18` and `2 ≤ k ≤ 10^18`. If `k` is greater than `2^n`, the function prints `1 1` and returns None. If `k` is less than or equal to `2^n`, it calculates values based on the number of 'total_days' which is `2^n`, computes a numerator and denominator in a loop, and then calculates two values `A` and `B` based on these computations. Finally, it prints the results of `A` and `B` modulo `1000003`. The function itself does not return any value.

