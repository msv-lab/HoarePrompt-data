#State of the program right berfore the function call: The function `func` is expected to take input through a predefined mechanism (e.g., standard input) and process multiple test cases. Each test case consists of four pairs of integers (x_i, y_i) representing the coordinates of the corners of a square, where -1000 <= x_i, y_i <= 1000. The number of test cases, t, is an integer such that 1 <= t <= 100. It is guaranteed that the given points form a square with sides parallel to the coordinate axes and with a positive area.
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
        
    #State: The loop has completed all iterations, and the value of `n` is 0. The values of `t` and `s` remain unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing the coordinates of the corners of a square. For each test case, it calculates and prints the area of the square. The function reads the number of test cases `n` from the input, and for each test case, it reads four pairs of integer coordinates. After processing all test cases, the value of `n` is 0, and the function concludes.

