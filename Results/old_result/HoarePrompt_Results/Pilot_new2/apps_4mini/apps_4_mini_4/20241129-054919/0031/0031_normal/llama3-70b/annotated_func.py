#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.
def func_1(n, k):
    total_days = 2 ** n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= total_days - i
        
        denominator *= total_days
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^{18}\), `k` is an integer such that \(2 \leq k \leq 10^{18}\), `total_days` is equal to \(2^n\), `numerator` is equal to \((2^n \cdot (2^n - 1) \cdot (2^n - 2) \cdots (2^n - (k - 1)))\), `denominator` is equal to \(2^{kn}\)
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    return numerator % (10 ** 6 + 3), denominator % (10 ** 6 + 3)
    #The program returns the updated numerator modulo (10
#Overall this is what the function does:The function accepts two integer parameters `n` and `k`, calculates the number of ways to select `k` distinct items from a set of size \(2^n\) using combinatorial logic, and returns the numerator and denominator of that calculation, both reduced by their greatest common divisor (gcd), modulo \(10^6 + 3\).

