#State of the program right berfore the function call: n is a non-negative integer.
def func_1(n):
    total = 0
    while n > 0:
        total += n % 10
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is 0, `total` is the sum of the digits of the original value of `n`
    return total
    #The program returns total, which is the sum of the digits of the original value of n, where n is 0. Therefore, total is 0.
#Overall this is what the function does:The function accepts a non-negative integer `n` and computes the sum of its digits. It utilizes a while loop to extract each digit by using the modulus operation and adding it to a total sum. The loop continues until all digits have been processed, ultimately terminating when `n` becomes zero. The function then returns the total sum of the digits. If `n` is initially zero, the function will return zero. The function does not handle negative integers or non-integer inputs, which may lead to unintended behavior if such inputs are passed.

