#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t testcases, x_i and y_i are integers such that -1000 <= x_i, y_i <= 1000, representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: The loop has executed `n` times, decrementing `n` by 1 each time until `n` reaches 0. For each iteration, the loop reads four pairs of coordinates, sorts them, calculates the area of the square formed by these coordinates, and prints the area rounded to the nearest integer. The value of `n` is now 0, and the values of `t`, `x_i`, and `y_i` remain unchanged.
#Overall this is what the function does:The function processes `t` test cases, where `t` is an integer between 1 and 100. For each test case, it reads four pairs of coordinates representing the corners of a square with sides parallel to the coordinate axes. It calculates the area of the square and prints the area rounded to the nearest integer. After processing all test cases, the value of `n` is 0, and the values of `t`, `x_i`, and `y_i` remain unchanged.

