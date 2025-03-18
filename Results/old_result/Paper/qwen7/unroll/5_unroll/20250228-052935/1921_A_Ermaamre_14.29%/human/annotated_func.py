#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer t (1 ≤ t ≤ 100), indicating the number of test cases. For each test case, there are four lines, each containing two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000), representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area. It is guaranteed that the given points form a valid square.
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
        
    #State: Output State: The output state will consist of a series of results, each being the square of the absolute difference in y-coordinates for specific pairs of points, based on the conditions provided within the loop. Each result is printed after the corresponding iteration of the loop. The number of results will be equal to the number of test cases (denoted by `a`).
#Overall this is what the function does:The function processes multiple test cases, where each test case involves four coordinates forming a square. For each test case, it calculates the absolute difference in y-coordinates for specific pairs of points and prints the square of this difference. The function does not return any value but outputs the results for each test case.

