#State of the program right berfore the function call: n is an integer greater than 1.
def func_1(n):
    """Check if a number is prime."""
    if (n < 2) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: n is an integer greater than 1, and n is not less than 2
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    #State of the program after the  for loop has been executed: `n` is an integer greater than 1, `i` is equal to `int(n
    return True
    #The program returns True
#Overall this is what the function does:The function accepts an integer `n` and returns `True` if `n` is a prime number (i.e., `n` is greater than 1 and has no divisors other than 1 and itself) and `False` otherwise (i.e., `n` is less than 2 or `n` has divisors other than 1 and itself)

#State of the program right berfore the function call: n is a positive integer.
def func_2(n):
    """Find the nth Newman-Shanks-Williams prime number."""
    if (n == 1) :
        return 7
        #The program returns 7
    #State of the program after the if block has been executed: n is a positive integer, and n is not equal to 1
    count = 1
    num = 7
    while True:
        if func_1(num):
            if num % 6 in [1, 5]:
                count += 1
                if count == n:
                    return num
        
        num += 1
        
    #State of the program after the loop has been executed: `count` equals the original value of `n`, `num` is the value that made `count` equal to `n` and satisfies `func_1(num)` being `True` and `num` modulo 6 being 1 or 5, assuming such a `num` exists; otherwise, the loop's behavior is undefined in this context.
#Overall this is what the function does:The function accepts a positive integer `n` and returns the `n`th Newman-Shanks-Williams prime number, which is 7 if `n` is 1, and for `n` greater than 1, it returns the `n`th number that is a prime and has a remainder of 1 or 5 when divided by 6, with undefined behavior for non-positive integers or non-integer inputs.

