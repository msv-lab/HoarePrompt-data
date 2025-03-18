#State of the program right berfore the function call: The function takes no input arguments but processes multiple test cases. Each test case consists of four lines, where each line contains two integers \(x_i, y_i\) such that \(-1000 \le x_i, y_i \le 1000\), representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area. There are at most 100 test cases.
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
        
    #State: Output State: `t` must be greater than 0, `steps` is equal to `t`, `a` is an input integer, `b` is an input integer, `c` is the first integer entered, `d` is the second integer entered, `e` is the third integer entered, `f` is the fourth integer entered, `g` is the fifth integer entered, `h` is the sixth integer entered, `n` is the minimum value between \((a - e)^2 + (b - f)^2\) and \((c - g)^2 + (d - h)^2\) after all iterations, `x` is the value of \((c - g)^2 + (d - h)^2\) from the last iteration.
    #
    #This means that after all iterations of the loop have finished, `t` will still be the initial number of test cases, `steps` will be equal to `t`, and the values of `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h` will be the most recently input integers. The variable `n` will hold the minimum value between the two distances calculated in each iteration, and `x` will hold the distance calculated in the last iteration, regardless of whether it was larger or smaller than `n`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of four pairs of integers representing the coordinates of the corners of a square. It calculates the squared distance between the diagonally opposite corners of the square and determines which of the two diagonals is shorter. For each test case, it prints the squared length of the shorter diagonal. After processing all test cases, the function does not return any value but outputs the results for each test case.

