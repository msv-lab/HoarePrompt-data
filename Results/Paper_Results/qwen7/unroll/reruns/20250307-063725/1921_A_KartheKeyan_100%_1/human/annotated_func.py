#State of the program right berfore the function call: There are four lines of input for each testcase, each containing two integers \(x_i, y_i\) such that \(-1000 \le x_i, y_i \le 1000\), representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area. There are \(t\) such testcases, where \(1 \le t \le 100\).
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
        
    #State: Output State: The output state will consist of `n` printed results from the loop, where each result is the rounded product of the Euclidean distances between specific pairs of points in a set of 4 points provided by the user. Each set of 4 points is sorted, and the distances between the first and second points and the third and fourth points are calculated. These distances are then multiplied together, and the square root of the product is taken before rounding to the nearest integer.
    #
    #The exact numerical values of the output depend on the input coordinates provided within each iteration of the loop. Since the problem does not specify any particular input values for `n` and `l`, or any specific sets of coordinates, the output can only be described in terms of its general form as outlined above.
#Overall this is what the function does:The function processes up to 100 test cases, where each test case consists of four pairs of coordinates \((x_i, y_i)\) representing the corners of a square. For each test case, it calculates the Euclidean distance between the first and second points and between the third and fourth points, multiplies these distances, takes the square root of the product, and rounds the result to the nearest integer. It then prints this rounded value for each test case.

