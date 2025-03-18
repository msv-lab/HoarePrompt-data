#State of the program right berfore the function call: There are four lines of input for each testcase, each containing two integers x_i, y_i such that -1000 ≤ x_i, y_i ≤ 1000. There are t testcases, where 1 ≤ t ≤ 100, and it is guaranteed that the given points form a square with sides parallel to the coordinate axes and a positive area.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: The output is the result of calculating \(dx \times dx\) for each test case, where \(dx\) is the difference between the maximum and minimum values in the first column of a 4x4 matrix provided for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four points forming a square with sides parallel to the coordinate axes. For each test case, it calculates and prints the area of the square by computing the square of the difference between the maximum and minimum x-coordinates of the given points.

