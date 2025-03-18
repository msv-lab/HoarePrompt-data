#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.
def func_1(n, k):
    total_days = 2 ** n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= total_days - i
        
        denominator *= total_days
        
    #State of the program after the  for loop has been executed: `numerator` is 0 if `k` is at least 3, `denominator` is `2^k`, `k` is at least 2.
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    return numerator % (10 ** 6 + 3), denominator % (10 ** 6 + 3)
    #The program returns (0 % (10
#Overall this is what the function does:The function accepts two integers `n` and `k`, calculates a `numerator` and `denominator` based on `total_days = 2^n`, and then returns the tuple containing `numerator % (10^6 + 3)` and `denominator % (10^6 + 3)`. However, if `k` is greater than or equal to 3, `numerator` becomes 0, leading to a return value of (0, denominator % (10^6 + 3)). Therefore, the function returns (0, denominator % (10^6 + 3)) when `k` is at least 3, effectively making `numerator` always zero in those cases.

