#State of the program right berfore the function call: The function should accept a list of test cases, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The coordinates satisfy -1000 <= x_i, y_i <= 1000, and the square has sides parallel to the coordinate axes with a positive area. The number of test cases, t, satisfies 1 <= t <= 100.
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
        
    #State: `n` is 0, `coord` is a sorted list containing four tuples `(x, y)`, `res` is the product of the square roots of `p1` and `p2`, `i` is 3, `x` and `y` are integers provided by the user, `p1` is the squared Euclidean distance between the first two tuples in `coord`, `p2` is the squared Euclidean distance between the third and fourth tuples in `coord`.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of four tuples representing the coordinates of the corners of a square. It calculates the product of the square roots of the squared Euclidean distances between specific pairs of coordinates and prints the rounded result for each test case. The function does not return any value; it only prints the results. After the function concludes, `n` is 0, and the program state includes the sorted list of coordinates `coord` and the calculated result `res` for the last test case.

