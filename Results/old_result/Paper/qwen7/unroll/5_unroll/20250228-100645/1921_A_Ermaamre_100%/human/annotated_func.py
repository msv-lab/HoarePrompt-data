#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer t (1 ≤ t ≤ 100), indicating the number of test cases. For each test case, there are four lines, each containing two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000), representing the coordinates of the corners of the square. It is guaranteed that these points form a square with sides parallel to the coordinate axes and a positive area.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: Output State: The value of `t` is a positive integer between 1 and 100, inclusive. For each iteration of the loop, a 4x2 matrix `a` is read from input, and `dx` is calculated as the square of the difference between the maximum and minimum values in the first column of `a`. The result `dx * dx` is printed for each iteration. After all iterations, the final value of `t` remains unchanged, but the printed output consists of the computed `dx * dx` values for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four pairs of integers representing the coordinates of the corners of a square. For each test case, it calculates the side length of the square and prints the area. The function does not return any value but outputs the area of each valid square found in the input.

