#State of the program right berfore the function call: The function takes no input parameters directly, but the input is provided through standard input in the format described. Each testcase consists of four lines, each containing two integers x_i, y_i representing the coordinates of the corners of the square. There are t test cases, where 1 ≤ t ≤ 100, and it is guaranteed that the given points form a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: Output State: The output state will be a list of results printed after each iteration of the loop.
    #
    #Explanation: The loop runs `n` times. In each iteration, it takes four pairs of coordinates as input, sorts them, calculates the distances between specific points, and then computes the product of the square roots of these distances. The result is printed after each calculation. Since the loop runs `n` times, there will be `n` printed results, each representing the computed value for that particular iteration.
#Overall this is what the function does:Functionality: The function processes up to 100 test cases, where each test case consists of four pairs of coordinates representing the corners of a square. It first sorts the coordinates, then calculates the distances between specific points, and finally computes the product of the square roots of these distances. The function prints the result for each test case, indicating whether the given points form a square with sides parallel to the coordinate axes and a positive area.

