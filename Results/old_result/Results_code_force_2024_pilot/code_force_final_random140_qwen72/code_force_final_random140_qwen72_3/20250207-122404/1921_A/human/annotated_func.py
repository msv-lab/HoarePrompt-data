#State of the program right berfore the function call: The function `func` is expected to take no arguments directly but should be designed to process multiple test cases. Each test case consists of four pairs of integers (x_i, y_i) representing the coordinates of the corners of a square, where -1000 <= x_i, y_i <= 1000. The number of test cases, t, is an integer such that 1 <= t <= 100. It is guaranteed that the given points form a square with sides parallel to the coordinate axes and with a positive area.
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
        
    #State: `t` is an integer such that 1 <= `t` <= 100, `steps` is `t-1`, `a` and `b` are the last set of input integers, `c` and `d` are the last set of input integers, `e` and `f` are the last set of input integers, `g` and `h` are the last set of input integers, `n` is `(a - c) * (a - c) + (b - d) * (b - d)`, `x` is `(a - e) * (a - e) + (b - f) * (b - f)`. If `x` > `n`, then `x` is greater than `n`. Otherwise, `x` is less than or equal to `n`.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of four pairs of integers representing the coordinates of the corners of a square. For each test case, it calculates two distances: one between the first and second pair of coordinates, and another between the first and third pair of coordinates. It then prints the smaller of these two squared distances. The function does not return any value; instead, it outputs the result directly to the console. After processing all test cases, the function concludes without modifying any global state or variables outside its scope.

