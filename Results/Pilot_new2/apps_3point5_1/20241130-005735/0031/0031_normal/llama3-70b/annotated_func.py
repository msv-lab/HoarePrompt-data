#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18.**
def func_1(n, k):
    total_days = 2 ** n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= total_days - i
        
        denominator *= total_days
        
    #State of the program after the  for loop has been executed: n and k are integers such that 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18, total_days = 2^n, numerator = (total_days - k)! * (total_days - (k-1))! * ... * (total_days - 1)!, denominator = 2^(k * n)
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    return numerator % (10 ** 6 + 3), denominator % (10 ** 6 + 3)
    #The program returns the remainder of numerator divided by (10
#Overall this is what the function does:The function `func_1` accepts two parameters, `n` and `k`, where both `n` and `k` are integers satisfying the constraints 1 ≤ n ≤ 10^18 and 2 ≤ k ≤ 10^18. The function calculates the remainder of the division of two numbers, numerator and denominator, based on the provided inputs. It then returns the remainder of the numerator divided by (10^6 + 3) and the remainder of the denominator divided by (10^6 + 3).

