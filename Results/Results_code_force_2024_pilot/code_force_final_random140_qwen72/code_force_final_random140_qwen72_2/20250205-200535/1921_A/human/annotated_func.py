#State of the program right berfore the function call: The function receives no direct parameters but operates under the assumption that the input is provided in a specific format. The input consists of multiple test cases, where the first line contains an integer t (1 ≤ t ≤ 100), indicating the number of test cases. Each test case is described by four lines, each containing two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000), representing the coordinates of the corners of a square with sides parallel to the coordinate axes. It is guaranteed that the points form a valid square with a positive area.
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
        
    #State: `t` is an integer between 1 and 100, inclusive, `steps` is `t-1`, `a` and `b` are the last set of input integers, `c` and `d` are the last set of input integers, `e` and `f` are the last set of input integers, `g` and `h` are the last set of input integers, `n` is `(a - c) * (a - c) + (b - d) * (b - d)`, `x` is `(a - e) * (a - e) + (b - f) * (b - f)`. After the if-else block, if `x` is greater than `n`, the current value of `x` remains greater than `n`. Otherwise, `x` is less than or equal to `n`.
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case consists of four pairs of integers representing the coordinates of the corners of a square. For each test case, it calculates the squared distances between two pairs of these coordinates and prints the smaller of the two squared distances. The function does not return any values; it only prints the results to the standard output. After processing all test cases, the function concludes without modifying any external state beyond the printed output.

