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
        
    #State of the program after the loop has been executed: `n` is 1, `count` is the sum of the values of `n // i` for all iterations until `n` becomes 1, and the loop has terminated.
    print(count)
#Overall this is what the function does:The function accepts a positive integer `n` (via user input) that must be at least 2 and calculates the sum of `n // i` for the largest divisor `i` of `n` (starting from 2) in each iteration until `n` reduces to 1. It prints the final sum, which is stored in `count`. The function does not explicitly return any value, as it only prints the result.

