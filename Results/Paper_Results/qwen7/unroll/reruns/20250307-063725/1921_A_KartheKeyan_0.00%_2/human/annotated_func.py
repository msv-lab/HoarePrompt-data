#State of the program right berfore the function call: There are four lines of input for each testcase, each containing two integers x_i, y_i representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area. There are t test cases, where 1 ≤ t ≤ 100, and -1000 ≤ x_i, y_i ≤ 1000.
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
        
    #State: Output State: The output state will consist of a series of floating-point numbers, each representing the result of the calculation for the distance product between two pairs of points from the input coordinates for each test case.
    #
    #Each line of the output will contain one such result, and the total number of lines will be equal to the initial value of `n`. The calculation performed for each test case involves sorting the input coordinates, then computing the Euclidean distances between the first and second points, and between the third and fourth points, and finally taking the absolute value of the product of these two distances.
#Overall this is what the function does:The function processes up to 100 test cases, where each test case consists of four integer coordinates (x_i, y_i) representing the corners of a square. It sorts these coordinates, calculates the Euclidean distances between the first and second points, and between the third and fourth points, and returns the absolute value of the product of these distances. The function outputs a series of floating-point numbers, each corresponding to the calculated distance product for each test case.

