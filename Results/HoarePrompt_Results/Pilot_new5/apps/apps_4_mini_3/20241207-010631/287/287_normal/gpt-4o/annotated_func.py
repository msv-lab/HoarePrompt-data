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
        
    #State of the program after the loop has been executed: `i` is greater than the square root of the original value of `num`, `count` is the total number of divisors of the original value of `num`, `num` remains the same as the initial value.
    return count
    #The program returns the total number of divisors of the original value of `num`
#Overall this is what the function does:The function accepts an integer `num` within the range of 1 to \(10^9\) and calculates the total number of divisors of `num`, returning this count. The function accounts for both the divisor and its complement (i.e., `num / i`) when `i` is not equal to `num // i`, ensuring all divisors are counted accurately.

