#State of the program right berfore the function call: The function processes multiple datasets of positive integers q, where 1 <= q < 2^31, and terminates when the input is -1. The number of datasets does not exceed 50.
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
        
    #State of the program after the  for loop has been executed: `q` is a positive integer input from the datasets, `x` is the cube root of `q` (accurate to within `q * 1e-05`), `diff` is equal to `q * 1e-05`, and the output is formatted to six decimal places.
#Overall this is what the function does:The function processes multiple datasets of positive integers, where each integer is read from the standard input until the input is -1, which terminates the process. For each positive integer `q`, it calculates the cube root of `q` using an iterative method that continues until the result is accurate to within `q * 1e-05`. The calculated cube root is then printed formatted to six decimal places. The function handles up to 50 datasets of integers and does not return any value; it only prints the results.

