#State of the program right berfore the function call: num is an integer such that 1 <= num <= 1000.
def func_1(num):
    if (num < 2) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: num is an integer such that 1 <= num <= 1000, and num is greater than or equal to 2
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `num` is either unchanged if it's a prime number and greater than or equal to 2, or the function returns `False` if `num` is not prime; `i` will be the last number checked before the function potentially returns `False` or completes the loop, indicating the highest divisor checked without finding `num` to be non-prime.
    return True
    #The program returns True, indicating that 'num' is a prime number greater than or equal to 2.
#Overall this is what the function does:The function `func_1` checks if a given integer `num` is a prime number and returns `True` if it is, `False` otherwise. It accepts an integer parameter `num` where `1 <= num <= 1000`. The function returns `False` for inputs less than 2, and for composite numbers (i.e., numbers that have divisors other than 1 and themselves). If `num` is a prime number greater than or equal to 2, the function returns `True`. The function handles all potential cases, including edge cases such as the smallest prime number (2) and the largest possible input (1000). Note that the function does not modify the input `num` and only returns a boolean value indicating whether `num` is prime or not.

