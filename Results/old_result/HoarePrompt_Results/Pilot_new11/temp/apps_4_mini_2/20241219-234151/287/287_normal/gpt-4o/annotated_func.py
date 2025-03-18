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
        
    #State of the program after the loop has been executed: 'i' is greater than or equal to the integer part of the square root of 'num' plus 1; `count` is the total number of divisors of 'num'. `i` is 'floor(sqrt(num)) + 1'.
    return count
    #The program returns the total number of divisors of 'num'
#Overall this is what the function does:The function `func_1` accepts a positive integer `num` (1 <= num <= 10^9) as input and calculates the total number of divisors of `num`. It iterates from 1 up to the square root of `num`, checking if each integer is a divisor. If a divisor is found, it increments a count and checks if the divisor pair (i, num // i) is distinct, incrementing the count again if so. The function returns the total count of divisors. After execution, the program's final state reflects that `count` holds the number of divisors of `num`, ensuring it handles the edge case where `num` is a perfect square correctly.

