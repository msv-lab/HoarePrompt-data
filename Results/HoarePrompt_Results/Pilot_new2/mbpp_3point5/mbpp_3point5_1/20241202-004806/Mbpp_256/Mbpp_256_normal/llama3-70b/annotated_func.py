#State of the program right berfore the function call: n is a non-negative integer.**
def func_1(n):
    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 3, `count` is the number of prime numbers between 2 and n (inclusive), `num` is n. If n is a prime number, `count` is increased by 1. Otherwise, `count` remains the same.
    return count
    #The program returns the number of prime numbers between 2 and n (inclusive), where n is a number greater than or equal to 3. If n itself is a prime number, the count is increased by 1.
#Overall this is what the function does:The function func_1 accepts a non-negative integer n and calculates the number of prime numbers between 2 and n (inclusive). If n itself is a prime number, the count is increased by 1. The function iterates through numbers from 2 to n (excluding n) and checks if each number is prime, incrementing the count accordingly. The function does not handle the case where n is less than 3 or negative numbers, which could lead to unexpected behavior.

#State of the program right berfore the function call: num is a non-negative integer.**
def is_prime(num):
    if (num < 2) :
        return False
        #The program returns False if num is less than 2, as per the initial state where num is a non-negative integer.
    #State of the program after the if block has been executed: *num is a non-negative integer. num is greater than or equal to 2
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `num` is a non-negative integer greater than or equal to 2, the square root of `num` is an integer, and `num` is a prime number. No changes are made to `num` or `i`.
    return True
    #The program returns True
#Overall this is what the function does:The `is_prime` function accepts a non-negative integer `num` as a parameter. It returns False if `num` is less than 2. Otherwise, it iterates through a range to check if `num` is divisible by any number in that range. If `num` is divisible by any number, the function returns False, indicating that `num` is not a prime number. If `num` is not divisible by any number in the range, the function returns True, indicating that `num` is a prime number.

