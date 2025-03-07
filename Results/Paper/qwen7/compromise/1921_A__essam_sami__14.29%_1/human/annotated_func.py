#State of the program right berfore the function call: There are four lines of input, each containing two integers x_i, y_i such that -1000 ≤ x_i, y_i ≤ 1000. These coordinates represent the corners of a square with sides parallel to the coordinate axes and a positive area. There are t test cases, where 1 ≤ t ≤ 100.
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
        
    #State: Output State: The output state will consist of a series of integers, each representing the minimum value between \(n\) and \(x\) for each iteration of the loop. Here, \(n\) is calculated as \((a - e)^2 + (b - f)^2\) and \(x\) is calculated as \((c - g)^2 + (d - h)^2\). For each test case, the program compares these two values and prints the smaller one.
#Overall this is what the function does:The function processes `t` test cases, where each test case involves four lines of input representing the coordinates of the corners of a square. For each test case, it calculates the squared distance between two pairs of opposite corners and prints the smaller distance. The function does not return any value but outputs the minimum distance for each test case.

