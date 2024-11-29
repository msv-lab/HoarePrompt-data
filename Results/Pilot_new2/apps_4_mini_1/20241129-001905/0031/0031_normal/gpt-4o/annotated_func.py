#State of the program right berfore the function call: n and k are integers where 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `b` is 0, `a` is the greatest common divisor (GCD) of the original values of `n` and `k`; the loop executes at least once if the original value of `b` is not 0.
    return a
    #The program returns the greatest common divisor (GCD) of the original values of n and k, denoted as 'a'
#Overall this is what the function does:The function accepts two integers `a` and `b`, and returns the greatest common divisor (GCD) of `a` and `b`. The function correctly computes the GCD using the Euclidean algorithm, and it handles cases where either `a` or `b` could be zero, as the loop will execute at least once if `b` is not initially zero. If both `a` and `b` are zero, the GCD is conventionally defined to be zero, but the function does not explicitly account for this scenario.

#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.
def func_2(n, k):
    MOD = 10 ** 6 + 3
    if (k > 1 << n) :
        print(1, 1)
        return
        #The program doesn't return any value as the return statement is empty
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ n ≤ 10^18; `k` is an integer such that 2 ≤ k ≤ 10^18; `MOD` is 1000003. The value of `k` is less than or equal to 1 << n.
    total_days = 1 << n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = numerator * (total_days - i) % MOD
        
        denominator = denominator * total_days % MOD
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 10^18, `k` is an integer such that 2 ≤ k ≤ 10^18, `MOD` is 1000003, `total_days` is 2, `numerator` is 0, `denominator` is 2^k % 1000003.
    p_no_shared = numerator
    p_total = denominator
    p_shared = (p_total - p_no_shared + MOD) % MOD
    A = p_shared
    B = p_total
    g = func_1(A, B)
    A //= g
    B //= g
    print(A % MOD, B % MOD)
#Overall this is what the function does:The function accepts two integers, `n` and `k`, where `1 ≤ n ≤ 10^18` and `2 ≤ k ≤ 10^18`. It calculates probabilities related to the distribution of `k` items over `2^n` total days modulo `1000003`. If `k` is greater than `2^n`, it prints (1, 1) and returns without performing further calculations. Otherwise, it computes the number of ways to choose `k` items from `2^n` total items, normalizes this fraction, and prints the resulting values modulo `1000003`. The function does not return any value.

