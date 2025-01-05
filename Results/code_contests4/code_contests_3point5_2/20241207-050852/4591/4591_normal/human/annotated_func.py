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
        
    #State of the program after the  for loop has been executed: After completing all iterations of the loop, `q` remains an integer, `diff` stays the same, `x` is the solution to the equation x^3 = q, and the formatted value of `x` is printed. The loop continues to execute until the absolute difference between the cube of `x` and `q` is less than `diff`, at which point the loop terminates.
#Overall this is what the function does:The function `func` reads input from standard input, calculates the cube root of the input using the Newton-Raphson method, and prints the result with 6 decimal places. The function does not accept any explicit parameters. The code handles the case where the input `q` is -1 to break out of the loop. It iterates until the absolute difference between the cube of `x` and `q` is less than `diff`. It accurately computes the cube root using the algorithm provided in the code.

