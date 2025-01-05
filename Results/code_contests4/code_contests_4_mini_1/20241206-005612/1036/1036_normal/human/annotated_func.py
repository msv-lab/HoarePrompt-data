#State of the program right berfore the function call: n is an integer greater than or equal to 2.
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
        
    #State of the program after the loop has been executed: `n` is 1, `count` is the sum of all b values from each iteration, `i` is the smallest integer that divides the last value of `n` before it became 1, `b` is 1.
    print(count)
#Overall this is what the function does:The function accepts no parameters and prompts the user for an integer input `n` (expected to be greater than or equal to 2). It then calculates a value `count`, which is the sum of the results of dividing `n` by its smallest divisor (greater than 1) until `n` becomes 1. The function prints the final value of `count`. If `n` is not a prime number, the loop continues until `n` is reduced to 1, accumulating the results of the divisions. However, if `n` is prime, the loop will break earlier once `b` equals 1. The function does not specify any output other than printing the `count`.

