#State of the program right berfore the function call: The function `func` is expected to take input parameters, but the function definition provided does not include any parameters. The correct function definition should include parameters for the number of test cases `t` and the coordinates of the corners of the square. Each test case consists of four pairs of integers (x_i, y_i) representing the coordinates of the corners of a square, where 1 ≤ t ≤ 100, and -1000 ≤ x_i, y_i ≤ 1000. The coordinates are guaranteed to form a square with sides parallel to the coordinate axes and with a positive area.
def func():
    """
    n = int(input())
     
    while n :
        
        l = int(input())
        s = 0
        s += (l//4)+(l-(4*(l//4)))//2
        print(s)
        n-=1
     
            
    """
    n = int(input())
    while n:
        coord = []
        
        res = 0
        
        for i in range(4):
            x, y = map(int, input().split())
            coord.append((x, y))
        
        coord = sorted(coord)
        
        p1 = (coord[1][0] - coord[0][0]) ** 2 + (coord[1][1] - coord[0][1]) ** 2
        
        p2 = (coord[3][0] - coord[2][0]) ** 2 + (coord[3][1] - coord[2][1]) ** 2
        
        res = math.sqrt(p1) * math.sqrt(p2)
        
        print(round(res))
        
        n -= 1
        
    #State: The loop has finished executing all iterations, and the variable `n` is now 0. The function `func` has not been called, and the state of other variables outside the loop remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, representing the number of test cases. For each test case, it reads four pairs of integers (x, y) representing the coordinates of the corners of a square. It then calculates the area of the square and prints the rounded value of this area. After processing all test cases, the variable `n` is 0, and the function has no return value. The state of other variables outside the function remains unchanged.

