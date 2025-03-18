#State of the program right berfore the function call: The function takes no input arguments. Each testcase consists of four lines, each containing two integers \(x_i, y_i\) such that \(-1000 \le x_i, y_i \le 1000\), representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area. There are \(t\) such testcases, where \(1 \le t \le 100\).
def func():
    t = int(input())
    for steps in range(t):
        a, b = map(int, input().split())
        
        c, d = map(int, input().split())
        
        e, f = map(int, input().split())
        
        g, h = map(int, input().split())
        
        n = (a - c) * (a - c) + (b - d) * (b - d)
        
        x = (a - e) * (a - e) + (b - f) * (b - f)
        
        if x > n:
            print(n)
        else:
            print(x)
        
    #State: Output State: `t` must be greater than 0, `steps` is equal to `t`, `a` is an input integer, `b` is an input integer, `c` is an input integer, `d` is an input integer, `e` is the first integer from the input split and converted to integer, `f` is the second integer from the input split and converted to integer, `g` is the first integer from the input split and converted to integer, `h` is the second integer from the input split and converted to integer, `n` is (a - c) * (a - c) + (b - d) * (b - d), `x` is (a - e) * (a - e) + (b - f) * (b - f). After all iterations, if any `x > n` during the loop, the maximum value among all `n` and `x` will be printed; otherwise, the minimum value among all `n` and `x` will be printed for each iteration.
    #
    #This means that after the loop completes all its iterations, the final output will be the maximum value of `n` or `x` encountered during the loop if there was at least one instance where `x > n`, otherwise, it will be the minimum value of `n` or `x` encountered.
#Overall this is what the function does:The function processes a series of test cases, each consisting of four lines with two integers representing the coordinates of the corners of a square. For each test case, it calculates the squared distance between the first and third corner, and the squared distance between the first and fourth corner. It then compares these distances and prints the maximum value found across all test cases. If no such maximum exists (i.e., all values are equal), it prints the minimum value instead. The function does not accept any parameters and does not return any value.

