#State of the program right berfore the function call: n is a positive integer such that 2 ≤ n ≤ 10^9.
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
        
    #State of the program after the loop has been executed: `n` is 1, `count` is the sum of all quotients `n // i` for the divisors `i` of the original value of `n`, where `i` is the smallest integer greater than 1 that divides `n`, and the loop terminates when `n` becomes 1.
    print(count)
#Overall this is what the function does:The function accepts a positive integer `n` (with the constraint 2 ≤ n ≤ 10^9) and calculates a cumulative count based on the quotients of `n` divided by its smallest divisor greater than 1, iterating until `n` reduces to 1. It prints the final count, which is the sum of all these quotients. However, the function does not return any value; it only prints the result.

