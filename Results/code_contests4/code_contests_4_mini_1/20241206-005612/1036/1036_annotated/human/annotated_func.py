#State of the program right berfore the function call: n is a positive integer such that n >= 2.
def func():
    n = int(raw_input())
    count = n
    while n != 1:
        for i in range(2, n):
            if divmod(n, i)[1] == 0:
                break
        
        b = n // i
        
        count += b
        
        n -= b
        
        if b == 1:
            break
        
    #State of the program after the loop has been executed: `n` is 1, `count` is the sum of all values `b` added during the loop iterations, `i` is the first number in the range [2, initial value of n) that divides the initial value of `n` if it exists, otherwise `i` is the initial value of `n`.
    print(count)
#Overall this is what the function does:The function accepts no parameters and reads a positive integer `n` from input (where `n >= 2`). It computes a value `count` by iteratively reducing `n` based on its divisors until `n` equals 1. During each iteration, it adds the quotient of `n` divided by the smallest divisor found to `count`. Finally, it prints the value of `count`. The function will effectively accumulate values based on the divisors of `n`, and it will terminate when `n` becomes 1.

