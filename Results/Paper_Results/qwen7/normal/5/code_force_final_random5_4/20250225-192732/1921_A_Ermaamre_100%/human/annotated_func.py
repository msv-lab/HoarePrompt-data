#State of the program right berfore the function call: There are four lines of input for each testcase, each containing two integers x_i, y_i such that -1000 ≤ x_i, y_i ≤ 1000. These coordinates represent the corners of a square with sides parallel to the coordinate axes and a positive area. There are t test cases, where 1 ≤ t ≤ 100.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: After all iterations of the loop have finished, `t` must be 0; `a` is a list of 4 lists, each containing integers entered by the user for each iteration, `x` is a list of the first elements from each of the 4 lists in `a` for each iteration, and `dx` is the difference between the maximum and minimum values in `x` for each iteration. The final output will consist of the value of `dx * dx` printed for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four pairs of integer coordinates representing the corners of a square. For each test case, it calculates the side length of the square and prints the area of the square (side length squared). The function reads the number of test cases from the input, then for each test case, it reads the coordinates, determines the side length, and outputs the area. After processing all test cases, the function concludes with no return value.

