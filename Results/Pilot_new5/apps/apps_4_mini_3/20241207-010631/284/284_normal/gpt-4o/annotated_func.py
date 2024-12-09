#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 1000.
def func_1(x):
    if (x <= 1) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 1000, and `x` is greater than 1.
    if (x <= 3) :
        return True
        #The program returns True
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 1000, and `x` is greater than 3.
    if (x % 2 == 0 or x % 3 == 0) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 1000, `x` is greater than 3, and `x` is neither divisible by 2 nor divisible by 3.
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        
        i += 6
        
    #State of the program after the loop has been executed: `i` is greater than the square root of `x`; `x` is greater than or equal to 121 and is neither divisible by 2 nor by 3, and not divisible by 5 or 7; the loop has concluded checking potential divisors of `x` up to its square root.
    return True
    #The program returns True, indicating that x is a prime number since it is not divisible by any potential divisors checked in the loop.
#Overall this is what the function does:The function accepts a positive integer `x` (where 1 ≤ x ≤ 1000) and checks if `x` is a prime number. It returns False for integers less than or equal to 1, returns True for 2 and 3, and returns False for even numbers greater than 2 and numbers divisible by 3. For odd integers greater than 3, it checks divisibility by potential prime factors up to the square root of `x`, returning True if `x` is prime and False if it is not.

