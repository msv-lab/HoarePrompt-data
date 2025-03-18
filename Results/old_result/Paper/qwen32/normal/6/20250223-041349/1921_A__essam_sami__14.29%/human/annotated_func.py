#State of the program right berfore the function call: There are t test cases (1 ≤ t ≤ 100), and for each test case, there are four lines containing the coordinates of the corners of a square (x_i, y_i) where -1000 ≤ x_i, y_i ≤ 1000. The coordinates represent a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: `t` is an input integer representing the number of test cases (1 ≤ t ≤ 100); the loop has executed `t` times; for each test case, the program has read four pairs of integers (`a`, `b`), (`c`, `d`), (`e`, `f`), and (`g`, `h`), calculated `n` as \((a - e) * (a - e) + (b - f) * (b - f)\) and `x` as \((c - g) * (c - g) + (d - h) * (d - h)\), and printed the smaller of `n` and `x`. The variable `steps` is equal to `t` after the loop completes.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of four lines representing the coordinates of the corners of a square with sides parallel to the coordinate axes. For each test case, it calculates the squared distance between two pairs of these corners and prints the smaller of the two squared distances.

