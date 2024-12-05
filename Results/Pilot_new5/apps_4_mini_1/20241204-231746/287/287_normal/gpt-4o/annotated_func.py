#State of the program right berfore the function call: num is an integer such that 1 <= num <= 10^9.
def func_1(num):
    count = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is greater than the square root of `num`, `count` is the total number of divisors of the original value of `num`, and if `num` is greater than or equal to 1, the loop executed at least once. If `num` is less than 1, the loop does not execute and `count` remains 0.
    return count
    #The program returns the total number of divisors of the original value of 'num'
#Overall this is what the function does:The function accepts an integer `num` (where 1 <= num <= 10^9) and returns the total number of divisors of `num` by iterating through all integers up to the square root of `num`. It counts both divisors `i` and `num // i` when `i` is a divisor, ensuring that duplicate divisors are only counted once. The function handles cases where `num` is a perfect square correctly by avoiding double counting.

