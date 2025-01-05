#State of the program right berfore the function call: q is a positive integer such that 1 <= q < 2^31.
def func():
    for line in stdin:
        q = int(line)
        
        if q == -1:
            break
        
        x = q / 2.0
        
        diff = q * 1e-05
        
        while True:
            x = x - (x ** 3 - q) / (3 * x * x)
            if abs(x ** 3 - q) < diff:
                break
        
        print('{:.6f}'.format(x))
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `q` remains a positive integer such that 1 <= q < 2^31, `x` is the approximate cube root of `q` formatted to 6 decimal places, `diff` is the value of `q` multiplied by 1e-05
#Overall this is what the function does:The function `func` reads input from stdin, calculates the approximate cube root of a positive integer `q`, and prints the result formatted to 6 decimal places. It continues this process until `-1` is entered as input. The function does not accept any parameters and iterates indefinitely until the break condition is met. If input is not a positive integer or `-1`, the behavior is not specified.

