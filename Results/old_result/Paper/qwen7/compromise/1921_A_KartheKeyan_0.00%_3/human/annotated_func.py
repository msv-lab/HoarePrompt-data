#State of the program right berfore the function call: There are four lines of input for each testcase, each containing two integers x_i, y_i such that -1000 ≤ x_i, y_i ≤ 1000. These coordinates represent the corners of a square with sides parallel to the coordinate axes and a positive area. There are t test cases, where 1 ≤ t ≤ 100.
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
        
        res = abs(math.sqrt(p1) * math.sqrt(p2))
        
        print(res)
        
        n -= 1
        
    #State: n is 0, coord is a list containing four tuples [ (x, y), (x, y), (x, y), (x, y) ], res is the absolute value of the product of the square roots of the sum of squared differences between the x-coordinates and y-coordinates of the first two points in coord and the sum of squared differences between the x-coordinates and y-coordinates of the last two points in coord, i is 6, p1 is (coord[1][0] - coord[0][0])
#Overall this is what the function does:The function processes up to 100 test cases, where each test case involves four lines of input representing the coordinates (x, y) of the corners of a square. For each test case, it calculates the area of the square formed by these coordinates and prints the result. After processing all test cases, the function ends with `n` set to 0, `coord` being a list of four coordinate tuples, `res` containing the calculated area, and `i` set to 6.

