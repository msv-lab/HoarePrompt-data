#State of the program right berfore the function call: The input consists of multiple test cases. Each test case has four lines, each containing two integers x_i, y_i such that -1000 ≤ x_i, y_i ≤ 1000. These coordinates represent the corners of a square with sides parallel to the coordinate axes and a positive area. There are at most 100 test cases.
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
        
    #State: Output State: The output state will consist of a series of numbers printed by the `print` statements inside the loop. For each iteration of the loop, the program calculates two distances `n` and `x`, and prints the smaller one. Therefore, the output will contain `t` numbers, where `t` is the number of test cases, and each number is the minimum distance calculated for each set of inputs provided by the user.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four pairs of coordinates representing the corners of a square. For each test case, it calculates the squared Euclidean distance between the diagonally opposite corners and prints the smaller distance. The function outputs a series of numbers, one for each test case, representing the minimum distance calculated for each set of input coordinates.

