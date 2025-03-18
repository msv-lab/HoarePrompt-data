#State of the program right berfore the function call: num is a positive integer between 1 and 10^9 (inclusive).
def func_1(num):
    count = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is the smallest integer greater than the square root of the original value of `num`, `count` is the total number of divisors of the original value of `num`, `num` remains unchanged
    return count
    #The program returns the total number of divisors of the original value of `num`
#Overall this is what the function does:The function accepts a positive integer `num` between 1 and 10^9 (inclusive) and returns the total number of divisors of `num`. The input `num` remains unchanged throughout the execution of the function. The function considers all divisors, including 1 and `num` itself, and counts each divisor only once. If `num` has a perfect square root, the function still counts its square root as a divisor. The function handles all potential edge cases, such as when `num` is a prime number (in which case it returns 2, for 1 and `num` itself) and when `num` is a perfect square (in which case its square root is counted as a divisor). The function's return value is an integer representing the total number of divisors of the original value of `num`.

