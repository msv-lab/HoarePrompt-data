#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. Each of the following t test cases consists of four lines, with each line containing two integers x_i and y_i such that -1000 <= x_i, y_i <= 1000. These integers represent the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: The printed areas of the squares for the `n` sets of coordinates processed by the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of the coordinates of the corners of a square. It calculates and prints the area of each square.

