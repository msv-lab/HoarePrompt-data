#State of the program right berfore the function call: There are four lines of input, each containing two integers \(x_i, y_i\) such that \(-1000 \le x_i, y_i \le 1000\), representing the coordinates of the corners of a square with sides parallel to the coordinate axes and a positive area.
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
        
    #State: Output State: `n` is 0, `x` is an input integer from the last iteration's third split, `y` is an input integer from the last iteration's third split, `coord` is a list containing four tuples of input integers sorted in ascending order, `p2` is the square of the difference between the x-coordinates of the last and second-to-last points in `coord`, `res` is the absolute value of the product of the square roots of `p1` and `p2`, `p1` is the square of the difference between the x-coordinates of the second and first points in `coord`.
    #
    #This means that after all iterations of the loop have finished, `n` will be reduced to 0. The variables `x` and `y` will hold the values from the last set of inputs provided. The list `coord` will contain four tuples representing the sorted coordinates of the corners of the last square input, and `res` will be the result calculated based on these coordinates.
#Overall this is what the function does:The function processes up to four sets of coordinates representing the corners of squares. For each set, it calculates the area of the square formed by these coordinates and prints the result. After processing all sets, it outputs the final calculated area and ensures that the loop counter `n` is reduced to 0. The function does not return any value but modifies variables like `coord`, `p1`, `p2`, and `res` to reflect the last processed square's properties.

