#State of the program right berfore the function call: The function should take an integer t (1 ≤ t ≤ 100) representing the number of test cases, and for each test case, it should take four pairs of integers (x_i, y_i) (-1000 ≤ x_i, y_i ≤ 1000) representing the coordinates of the corners of a square with sides parallel to the coordinate axes. The coordinates are given in random order, and it is guaranteed that the points form a square with a positive area.
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
        
    #State: The loop has finished executing, and the value of `n` is 0. The variables `coord` and `res` are reset to their initial states (empty list and 0, respectively) at the beginning of each iteration, so they do not retain any values after the loop. The coordinates of the corners of the square and the initial value of `t` remain unchanged.
#Overall this is what the function does:The function `func` accepts an integer `t` (1 ≤ t ≤ 100) representing the number of test cases. For each test case, it accepts four pairs of integers `(x_i, y_i)` (-1000 ≤ x_i, y_i ≤ 1000) representing the coordinates of the corners of a square with sides parallel to the coordinate axes. The function calculates and prints the area of the square for each test case. After processing all test cases, the value of `t` is 0, and the function concludes without returning any value. The coordinates of the corners of the square and the initial value of `t` remain unchanged.

