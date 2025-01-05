#State of the program right berfore the function call: The input consists of multiple positive integers q (1 <= q < 2^31), with -1 indicating the end of the input. The function does not take any parameters and handles inputs from standard input.
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
        
    #State of the program after the  for loop has been executed: `q` is a positive integer, `x` is the cube root of `q`, `diff` is a positive float equal to `q * 1e-05`. The value of `x` is printed formatted to six decimal places for each positive integer input before `-1`.
#Overall this is what the function does:The function reads multiple positive integers from standard input until it encounters -1, which signals the termination of input. For each positive integer `q`, it calculates the cube root of `q` using an iterative method and prints the result formatted to six decimal places. The function does not return any value; it simply outputs the cube roots for each valid integer input.

