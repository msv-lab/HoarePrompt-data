#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each of the t test cases, there are four pairs of integers (x_i, y_i) where -1000 <= x_i, y_i <= 1000, representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: `t` is an integer such that 1 <= t <= 100; `n` is 0; `coord` is a sorted list of the last set of four tuples `((x1, y1), (x2, y2), (x3, y3), (x4, y4))` read in the last iteration; `res` is the product of the square roots of `p1` and `p2` from the last iteration; `i` is 3; `p1` is \((coord[1][0] - coord[0][0])^2 + (coord[1][1] - coord[0][1])^2\) from the last iteration; `p2` is \((coord[3][0] - coord[2][0])^2 + (coord[3][1] - coord[2][1])^2\) from the last iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads four pairs of integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes. It calculates and prints the side length of the square for each test case.

