#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.**
def func_1(n, k):
    total_days = 2 ** n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= total_days - i
        
        denominator *= total_days
        
    #State of the program after the  for loop has been executed: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18; total_days is 2 to the power of n; numerator is the product of (total_days - i) for i from 0 to k-1; denominator is the product of total_days for i from 0 to k-1
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    return numerator % (10 ** 6 + 3), denominator % (10 ** 6 + 3)
    #The program returns the remainder of the division of numerator by (10
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, both of which are integers satisfying the constraints 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18. It calculates the remainder of the division of the numerator by (10^6 + 3) and the denominator by (10^6 + 3), where the numerator is the product of (total_days - i) for i from 0 to k-1, the denominator is the product of total_days for i from 0 to k-1, and total_days is 2 raised to the power of n.

