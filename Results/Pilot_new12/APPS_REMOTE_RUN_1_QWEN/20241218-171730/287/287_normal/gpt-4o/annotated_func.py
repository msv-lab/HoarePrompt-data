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
        
    #State of the program after the loop has been executed: `num` is an integer such that \(1 \leq num \leq 10^9\), `count` is the number of distinct divisors of `num` including 1 and `num` itself, `i` is the square root of `num` rounded up to the nearest integer.
    return count
    #The program returns count which is the number of distinct divisors of num including 1 and num itself
#Overall this is what the function does:The function `func_1` accepts an integer `num` where \(1 \leq num \leq 10^9\) and returns the count of its distinct divisors, including 1 and `num` itself. The function iterates from 1 to the square root of `num`, checking for divisors. If `i` is a divisor of `num`, both `i` and `num // i` (if they are not equal) are counted as distinct divisors. The function handles the edge case where `num` is a perfect square by ensuring that the square root is only counted once.

