#State of the program right berfore the function call: The input consists of several test cases. The first line contains an integer t (1 ≤ t ≤ 100) representing the number of test cases. Each test case consists of four lines, with each line containing two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000) representing the coordinates of the corners of a square. It is guaranteed that the given points form a square with sides parallel to the coordinate axes and a positive (strictly greater than 0) area.
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
        
    #State: The value of `n` is 0, and the values of `coord`, `res`, `p1`, and `p2` are not retained. The rounded areas of the squares for each test case have been printed.
#Overall this is what the function does:The function accepts multiple test cases, where each test case consists of four pairs of integers representing the coordinates of the corners of a square with sides parallel to the coordinate axes. For each test case, the function calculates and prints the area of the square.

