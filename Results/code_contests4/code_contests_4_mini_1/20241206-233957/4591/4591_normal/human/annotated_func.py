#State of the program right berfore the function call: The input consists of multiple datasets where each dataset is a positive integer q (1 <= q < 2^31), and the input ends with -1. The function will process at most 50 datasets.
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
        
    #State of the program after the  for loop has been executed: `line` is the last positive integer processed before -1, `q` is the last positive integer processed before -1, `x` is the cube root of `q`, `diff` is equal to `q * 1e-05`, the value of `x` is printed formatted to six decimal places.
#Overall this is what the function does:The function reads multiple positive integer datasets (up to 50), terminating input upon receiving -1. For each positive integer `q`, it calculates the cube root of `q` using an iterative method, and prints the result formatted to six decimal places. The function does not accept parameters and does not return any value. It assumes valid input and does not handle the case of invalid integers or data types.

