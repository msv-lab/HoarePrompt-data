#State of the program right berfore the function call: The function takes no input parameters. Each testcase consists of four lines, each containing two integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area. There are t testcases, where 1 ≤ t ≤ 100.
def func():
    a = int(input())
    for i in range(a):
        x1, y1 = map(int, input().split())
        
        x2, y2 = map(int, input().split())
        
        x3, y3 = map(int, input().split())
        
        x4, y4 = map(int, input().split())
        
        if x1 == x3 and x2 == x4:
            if y1 < y3:
                res = abs(y3 - y1)
            else:
                res = abs(y1 - y3)
        elif x1 == x2 and x3 == x4:
            if y1 < y2:
                res = abs(y2 - y1)
            else:
                res = abs(y1 - y2)
        elif x1 == x4 and x3 == x2:
            if y1 < y2:
                res = abs(y2 - y1)
            else:
                res = abs(y1 - y2)
        
        print(res ** 2)
        
    #State: After all iterations of the loop have finished, the variable `i` will be equal to `a-1`, and `res` will hold the result of the last calculation performed within the loop based on the conditions provided. The values of `x1`, `y1`, `x2`, `y2`, `x3`, `y3`, and `x4`, `y4` will be those provided by the last set of inputs processed by the loop.
#Overall this is what the function does:The function processes up to 100 test cases, where each test case involves four lines of input representing the coordinates of the corners of a square. Based on specific conditions related to the coordinates, it calculates the height of the square and prints the square of this height. The function does not return any value.

