#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.**
def func_1(n, k):
    total_days = 2 ** n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= total_days - i
        
        denominator *= total_days
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 10^18, `k` is an integer such that 2 ≤ k ≤ 10^18, `total_days` is 2 raised to the power of n, `numerator` is equal to the product of (total_days - k + 1) to (total_days - 1), `denominator` is 2 raised to the power of n multiplied by total_days, `i` is k-1, `k` must be greater than 0
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    return numerator % (10 ** 6 + 3), denominator % (10 ** 6 + 3)
    #The program returns the remainder of numerator divided by (10
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where `n` and `k` are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18. It calculates the values of `numerator` and `denominator` based on the given formula. Then, it calculates the greatest common divisor (gcd) of `numerator` and `denominator`, and updates the values of `numerator` and `denominator` accordingly. Finally, it returns the remainders of `numerator` and `denominator` divided by (10^6 + 3).

