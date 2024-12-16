#State of the program right berfore the function call: num is an integer such that 1 <= num <= 1000.
def func_1(num):
    if (num < 2) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: num is an integer such that 1 <= num <= 1000, and num is greater than or equal to 2
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `num` is a prime number within the range [2, 1000], and `i` is equal to the square root of `num` (if `num` is a perfect square) or the largest integer less than the square root of `num` (if `num` is not a perfect square), indicating that `num` has been checked for divisibility up to its square root and found to be prime.
    return True
    #The program returns True, indicating that `num` is a prime number within the range [2, 1000]
#Overall this is what the function does:The function accepts an integer `num` and returns True if `num` is a prime number greater than or equal to 2, False if `num` is less than 2 or has any divisors other than 1 and itself

