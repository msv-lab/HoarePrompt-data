#State of the program right berfore the function call: num is a positive integer such that 1 ≤ num ≤ 1000.
def func_1(num):
    if (num < 2) :
        return False
        #The program returns False since the current value of num is less than 2 and num is a positive integer such that 1 ≤ num ≤ 1000.
    #State of the program after the if block has been executed: *`num` is a positive integer such that 1 ≤ `num` ≤ 1000 and `num` is greater than or equal to 2.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `num` is a positive integer greater than or equal to 2, and `i` is such that if the loop completes all iterations without returning, then `num` is determined to be a prime number. If the loop finds a divisor, `num` is not prime, and the function returns `False`.
    return True
    #The program returns True, indicating that num is a prime number since the loop has completed all iterations without finding a divisor.
#Overall this is what the function does:The function accepts a positive integer `num` such that \(1 \leq num \leq 1000\). It returns `False` if `num` is less than 2 or if `num` is found to be divisible by any integer in the range from 2 to the square root of `num`. If no divisors are found in that range, it returns `True`, indicating that `num` is a prime number. Note that the function does not handle cases where `num` is exactly equal to 1, which is not a prime number but falls within the specified input range. Additionally, if `num` is less than 2, the function will correctly return `False` without further checks.

