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
        
    #State of the program after the  for loop has been executed: After the loop executes, `q` remains a positive integer such that 1 <= q < 2^31, `x` is the final value that satisfies abs(x^3 - q) < diff, with x printed with 6 decimal places, and `diff` remains unchanged.
#Overall this is what the function does:The function `func` reads input from standard input, calculates a value `x` iteratively using the Newton-Raphson method to find the cube root of the input `q`, and prints the result with 6 decimal places. The function does not accept any parameters. The code seems to handle the case where the input value `q` is -1 to exit the loop. However, the return value or output of the function is not explicitly defined in the annotations.

