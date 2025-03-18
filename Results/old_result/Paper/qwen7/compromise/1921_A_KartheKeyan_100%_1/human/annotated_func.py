#State of the program right berfore the function call: There are four lines, each containing two integers \(x_i, y_i\) such that \(-1000 \le x_i, y_i \le 1000\), representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: Output State: `n` is 0, `total` is 0, `coord` is a list containing four tuples sorted by their first elements, each tuple representing the (x, y) coordinates provided as input, `i` is 3, `x` is the last input integer, `y` is the last input integer, `p1` is (input integer - `x`)² + (input integer - `y`)², `p2` is ((input integer - `x`)² + (input integer - `y`)²), `res` is sqrt((input integer - `x`)² + (input integer - `y`)²) * sqrt(((input integer - `x`)² + (input integer - `y`)²)).
    #
    #Explanation: After all iterations of the loop have finished, `n` will be decremented to 0 since it starts at a value greater than 0 and is decreased by 1 in each iteration until it reaches 0. The variable `total` is not mentioned in the loop body or head, so it remains 0. The variable `coord` will contain the coordinates provided as input, sorted by their first elements, after all iterations. The variable `i` will be 3 because the for loop runs 4 times for each iteration of the while loop. The variables `x` and `y` will hold the last set of coordinates provided as input, and `p1` and `p2` will be calculated based on these last coordinates. The variable `res` will be the final result printed after the last iteration, which is the product of the square roots of `p1` and `p2`.
#Overall this is what the function does:The function processes a series of square coordinates provided as input. For each set of coordinates, it calculates the side length of the square and prints the product of the square roots of the distances between the first and second corner and the third and fourth corner. After processing all sets of coordinates, the function ensures that the loop counter `n` is decremented to 0.

