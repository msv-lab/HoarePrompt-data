#State of the program right berfore the function call: There are t test cases (1 ≤ t ≤ 100). For each test case, there are four lines of input, each containing two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000) representing the coordinates of the corners of a square with sides parallel to the coordinate axes and positive area.
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
        
    #State: `n` is 0, `coord` is a sorted list of tuples `((x1, y1), (x2, y2), (x3, y3), (x4, y4))` based on the last set of input coordinates, `res` is `abs(math.sqrt(p1) * math.sqrt(p2))` for the last set of coordinates, `p1` is `(coord[1][0] - coord[0][0])
#Overall this is what the function does:The function accepts `t` test cases, where each test case consists of four pairs of integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes and positive area. For each test case, the function calculates and prints the area of the square.

