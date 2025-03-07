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
        
    #State: `t` is an integer such that 1 <= t <= 100; `n` is 0; `l` and `s` are not retained after the loop ends.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases. For each test case, it receives four pairs of integers `(x_i, y_i)` that denote the coordinates of the corners of a square. The function calculates and prints the area of each square.

