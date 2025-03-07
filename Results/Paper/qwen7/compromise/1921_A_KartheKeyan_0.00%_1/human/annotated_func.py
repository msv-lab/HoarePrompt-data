#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer t (1 ≤ t ≤ 100), indicating the number of test cases. For each test case, there are four lines, each containing two integers x_i, y_i (-1000 ≤ x_i, y_i ≤ 1000), representing the coordinates of the corners of the square. It is guaranteed that these points form a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: Output State: `n` is 0, `s` is the sum of the results from all iterations of the loop, and we have processed `t` test cases.
    #
    #Explanation: After the loop has executed all its iterations, `n` will be 0 because the loop continues as long as `n` is non-zero. The variable `s` will be the cumulative sum of the results (`res`) from each iteration of the loop. Since the loop processes each test case completely before moving on to the next, and we started with processing `t-1` test cases, after all iterations, we would have processed `t` test cases.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of coordinates for the corners of a square. It calculates the area of the square formed by these coordinates and prints the result for each test case. After processing all test cases, it ensures that the counter `n` is set to 0.

