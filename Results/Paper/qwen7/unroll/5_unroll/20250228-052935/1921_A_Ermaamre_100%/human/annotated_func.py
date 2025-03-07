#State of the program right berfore the function call: There are four lines of input for each testcase, each containing two integers x_i, y_i such that -1000 ≤ x_i, y_i ≤ 1000. These coordinates represent the corners of a square with sides parallel to the coordinate axes and a positive area. There are t test cases, where 1 ≤ t ≤ 100.
def func():
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: The output is the result of calculating \(dx \times dx\) for each test case, where \(dx\) is the difference between the maximum and minimum values in the first column of a 4x4 matrix provided by the user. The process is repeated for each of the \(t\) test cases.
#Overall this is what the function does:The function processes up to 100 test cases, where each test case involves four lines of input representing the coordinates of the corners of a square. For each test case, it calculates the difference between the maximum and minimum x-coordinates of the given points and prints the square of this difference. The function does not return any value but outputs the calculated result for each test case.

