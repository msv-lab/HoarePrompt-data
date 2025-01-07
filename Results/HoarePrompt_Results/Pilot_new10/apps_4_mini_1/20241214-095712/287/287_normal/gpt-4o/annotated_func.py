#State of the program right berfore the function call: num is a positive integer such that 1 <= num <= 10^9.
def func_1(num):
    count = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is incremented to the smallest integer greater than the square root of `num`, `count` is the total number of divisors of the original value of `num`
    return count
    #The program returns the total number of divisors of the original value of 'num'
#Overall this is what the function does:The function accepts a positive integer `num` and returns the total number of divisors of `num`. It correctly counts each divisor pair, ensuring not to double count when the divisor is the square root of `num`.

