#State of the program right berfore the function call: The function should accept a list of test cases, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The coordinates (x_i, y_i) satisfy -1000 <= x_i, y_i <= 1000, and the number of test cases t satisfies 1 <= t <= 100. Each test case guarantees the existence of a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: `total` is 0, `coord` is a sorted list with 4 elements, `res` is `math.sqrt(coord[1][0] - coord[0][0]) * math.sqrt(coord[3][0] - coord[2][0])`, `x` is an input integer, `y` is an input integer, `p1` is `(coord[1][0] - coord[0][0])`, `p2` is `(coord[3][0] - coord[2][0])`, `n` is 0.
#Overall this is what the function does:The function reads an integer `n` indicating the number of test cases. For each test case, it reads four pairs of integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes. It calculates and prints the area of each square. After processing all test cases, `n` is 0, and the function concludes.

