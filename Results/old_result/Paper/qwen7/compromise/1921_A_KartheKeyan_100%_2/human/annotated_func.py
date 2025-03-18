#State of the program right berfore the function call: There are four lines of input, each containing two integers x_i, y_i such that -1000 ≤ x_i, y_i ≤ 1000. These coordinates represent the corners of a square with sides parallel to the coordinate axes and a positive area. There are t such sets of coordinates, where 1 ≤ t ≤ 100.
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
        
    #State: Output State: `i` is 12, `n` is 0, `x` is an input integer, `y` is an input integer, `coord` is a list containing four tuples `[('input integer', 'input integer'), ('input integer', 'input integer'), ('input integer', 'input integer'), ('input integer', 'input integer')], `p2` is (coord[3][0] - coord[2][0]), `res` is math.sqrt(coord[3][0] - coord[2][0])
    #
    #Explanation: After the loop has executed all its iterations, the variable `n` will be decremented to 0 since it starts as an input integer and decreases by 1 with each iteration until it reaches 0. The variable `i` will be 12 because it increments by 4 in each iteration (as there are 4 iterations per loop) and the loop runs 3 times, so \(3 \times 4 = 12\). The value of `x` and `y` remains as input integers from the last iteration, and `coord` contains the coordinates entered in the last iteration. The values of `p2` and `res` are calculated based on the last set of coordinates entered.
#Overall this is what the function does:The function processes up to 100 sets of coordinates, each representing the corners of a square with sides parallel to the coordinate axes. For each set, it calculates the side lengths of the square and then computes the product of these side lengths to determine the area. Finally, it prints the rounded area for each square.

