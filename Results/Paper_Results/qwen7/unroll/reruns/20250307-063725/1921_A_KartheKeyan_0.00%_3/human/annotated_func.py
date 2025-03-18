#State of the program right berfore the function call: The function takes no input parameters directly, but the input is read from standard input. Each testcase consists of four lines, each containing two integers x_i, y_i, representing the coordinates of the corners of the square. There are t testcases, where 1 ≤ t ≤ 100, and for each testcase, the coordinates provided form a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: Output State: The output state will consist of a series of printed results, each representing the computed value of `res` for each iteration of the loop.
    #
    #Explanation: For each iteration of the loop, the code processes four pairs of coordinates (input by the user), sorts them, calculates the squared distances between specific points, computes the product of the square roots of these distances, and then prints the absolute value of this product. This process repeats `n` times, with `n` being the initial input integer. Each printed result corresponds to the value of `res` for that particular iteration.
#Overall this is what the function does:Functionality: The function reads a series of testcases from standard input, where each testcase consists of four pairs of coordinates representing the corners of a square. It processes each testcase to calculate the area of the square formed by these coordinates. Specifically, it sorts the coordinates, computes the squared distances between specific points, finds the product of the square roots of these distances, and prints the absolute value of this product for each testcase. After processing all testcases, the function concludes with a series of printed outputs, each representing the calculated area of the square for that testcase.

