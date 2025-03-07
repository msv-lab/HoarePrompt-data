#State of the program right berfore the function call: The function takes no input parameters. Each testcase consists of four lines, each containing two integers x_i, y_i (-1000 \le x_i, y_i \le 1000), representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area. There are t (1 \le t \le 100) such testcases.
def func():
    t = int(input())
    for steps in range(t):
        a, b = map(int, input().split())
        
        c, d = map(int, input().split())
        
        e, f = map(int, input().split())
        
        g, h = map(int, input().split())
        
        n = (a - e) * (a - e) + (b - f) * (b - f)
        
        x = (c - g) * (c - g) + (d - h) * (d - h)
        
        if x > n:
            print(n)
        else:
            print(x)
        
    #State: After the loop executes all iterations, `t` must be greater than 0, `steps` will be equal to `t-1`, `a` and `b` will be the last two integers entered by the user, `c` and `d` will be the integers entered in the first input, `e` and `f` will be the integers from the second input split, `g` and `h` will be the integers from the last input split. The variable `n` will be the value of \((a - e) * (a - e) + (b - f) * (b - b)\) calculated in the last iteration, and `x` will be the value of \((c - g) * (c - g) + (d - h) * (d - h)\) calculated in the last iteration. Depending on whether `x` is greater than `n`, either `n` or `x` will be printed in each iteration.
#Overall this is what the function does:The function processes up to 100 test cases, where each test case consists of four lines of input, each containing two integers representing the coordinates of the corners of a square. For each test case, it calculates the squared distance between the diagonally opposite corners and prints the smaller of the two distances.

