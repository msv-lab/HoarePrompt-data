#State of the program right berfore the function call: The function takes no input arguments. Each testcase consists of four lines, each containing two integers x_i, y_i representing the coordinates of the corners of the square. The coordinates satisfy -1000 ≤ x_i, y_i ≤ 1000, and it is guaranteed that these points form a square with sides parallel to the coordinate axes and a positive area. There are t testcases, where 1 ≤ t ≤ 100.
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
        
    #State: Output State: The output state will consist of a series of integers printed during each iteration of the loop. For each test case (iteration), the program calculates two distances \(n\) and \(x\), and prints the smaller one. The specific values printed will depend on the inputs provided for each test case.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of four pairs of integer coordinates representing the corners of a square. For each test case, it calculates the squared distance between two opposite corners and compares them. It then prints the smaller squared distance. The function does not return any value but outputs the results for each test case.

