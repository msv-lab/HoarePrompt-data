#State of the program right berfore the function call: The function should accept a list of test cases, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The coordinates x_i and y_i are within the range -1000 to 1000, inclusive, and the number of test cases t is an integer such that 1 <= t <= 100. The coordinates are guaranteed to form a square with sides parallel to the coordinate axes and with a positive area.
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
        
    #State: `n` is 0, `coord` is a sorted list containing four tuples `(x, y)` from the last iteration, `res` is the product of the square roots of the squared distances between the first and second points and the third and fourth points in `coord`, `i` is 3, `range` is 4, `x` and `y` are the last input integers, `p1` is the squared distance between the first and second points in `coord`, `p2` is the squared distance between the third and fourth points in `coord`.
#Overall this is what the function does:The function reads an integer `n` indicating the number of test cases. For each test case, it reads four pairs of integers representing the coordinates of the corners of a square. It calculates the area of the square and prints it. After processing all test cases, the function terminates with `n` being 0, and the last processed square's coordinates and area calculation variables (`coord`, `p1`, `p2`, `res`) holding the state from the final iteration.

