#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^9.**
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
        
    #State of the program after the loop has been executed: `n` is 1, `count` is the sum of all previous values of `n` divided by 2, `b` is 1
    print(count)
#Overall this is what the function does:The function does not accept any parameters. It reads an integer `n` from the user and performs a series of calculations based on the value of `n`. It calculates the sum of all previous values of `n` divided by 2 while `n` is not equal to 1. The function then prints the final calculated sum. The code does not handle any constraints related to the range of `n` (2 <= n <= 10^9) as indicated in the annotation. Additionally, the functionality does not provide any return value.

