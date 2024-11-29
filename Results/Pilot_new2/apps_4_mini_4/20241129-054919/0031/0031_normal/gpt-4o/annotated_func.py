#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `b` is 0, `a` is the GCD of the original values of 'n' and 'k'
    return a
    #The program returns a, which is the GCD of the original values of 'n' and 'k'
#Overall this is what the function does:The function accepts two integer parameters `a` and `b`, and returns the greatest common divisor (GCD) of the two integers using the Euclidean algorithm. It handles all valid integer inputs within the specified range and reliably computes the GCD, as `b` will eventually become zero, at which point `a` contains the GCD of the original values.

#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.
def func_2(n, k):
    MOD = 10 ** 6 + 3
    if (k > 1 << n) :
        print(1, 1)
        return
        #The program returns None as no value is specified to be returned
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ n ≤ 10^18, `k` is an integer such that 2 ≤ k ≤ 10^18, `MOD` is 1000003, and `k` is less than or equal to 1 shifted left by `n` (k ≤ 2^n)
    total_days = 1 << n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = numerator * (total_days - i) % MOD
        
        denominator = denominator * total_days % MOD
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 10^18, `k` is an integer such that 2 ≤ k ≤ 10^18, `MOD` is 1000003, `total_days` is equal to `2^n`, `numerator` is equal to the product of `(2^n - i) % 1000003` for `i` in the range from 0 to `k-1`, and `denominator` is equal to `(2^n)^k % 1000003.
    p_no_shared = numerator
    p_total = denominator
    p_shared = (p_total - p_no_shared + MOD) % MOD
    A = p_shared
    B = p_total
    g = func_1(A, B)
    A //= g
    B //= g
    print(A % MOD, B % MOD)
#Overall this is what the function does:The function accepts two integer parameters `n` and `k`, where `1 ≤ n ≤ 10^18` and `2 ≤ k ≤ 10^18`. It calculates the number of ways to choose `k` items from a set of size `2^n` modulo `1000003`. If `k` exceeds `2^n`, it prints `1 1` and returns without further computation. The calculation involves the product of decreasing values from `2^n` for `k` iterations and does not return a value; instead, it prints the result.

