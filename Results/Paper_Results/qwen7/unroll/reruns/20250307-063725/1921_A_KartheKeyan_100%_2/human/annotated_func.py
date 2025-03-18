#State of the program right berfore the function call: There are four lines of input for each testcase, each containing two integers x_i, y_i representing the coordinates of the corners of a square. The coordinates satisfy -1000 ≤ x_i, y_i ≤ 1000. It is guaranteed that there exists a square with sides parallel to the coordinate axes and a positive area among the given points.
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
        
    #State: Output State: The output state will consist of a series of printed results, each being the rounded geometric mean of the distances between two pairs of points from four given points. The number of such results will be equal to the initial value of `n`.
    #
    #To break it down:
    #1. The loop runs `n` times.
    #2. In each iteration, the user is expected to provide coordinates for four points.
    #3. These points are sorted.
    #4. The distances between the first and second points, and the third and fourth points are calculated.
    #5. The geometric mean of these distances is computed and printed.
    #6. After printing, `n` is decremented by 1.
    #
    #The final output state will be a list of `n` numbers, each representing the rounded geometric mean of the distances as described above.
#Overall this is what the function does:The function processes multiple test cases, where each case consists of four pairs of coordinates (x_i, y_i) representing the corners of a square. It calculates and prints the rounded geometric mean of the distances between the first and second points, and the third and fourth points for each case. The function continues until all test cases are processed.

