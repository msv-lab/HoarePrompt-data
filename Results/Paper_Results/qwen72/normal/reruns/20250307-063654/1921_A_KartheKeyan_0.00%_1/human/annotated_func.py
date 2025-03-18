#State of the program right berfore the function call: The function `func` is expected to take no input parameters, but based on the problem description, it should be modified to accept a list of test cases, where each test case is a list of four tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The coordinates satisfy -1000 <= x_i, y_i <= 1000, and there is at least one square with sides parallel to the coordinate axes and a positive area. The number of test cases, t, satisfies 1 <= t <= 100.
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
        
    #State: `n` is 0, `func` is expected to take a list of test cases where each test case is a list of four tuples representing the coordinates of the corners of a square, `coord` is a sorted list containing four tuples `(x, y)` appended in the order they were input, `res` is the absolute value of the product of the square roots of `p1` and `p2`, `i` is 3, `x` and `y` are updated to the input integers provided by the user, `p1` is the squared distance between the first and second coordinates in the sorted `coord` list, `p2` is the squared distance between the third and fourth coordinates in the sorted `coord` list.
#Overall this is what the function does:The function `func` reads an integer `n` from the user, indicating the number of test cases. For each test case, it reads four pairs of integers (coordinates) from the user, sorts these coordinates, and calculates a value `res` based on the squared distances between specific pairs of coordinates. The function then prints `res` for each test case. After processing all test cases, the function terminates with `n` being 0. The function does not return any value.

