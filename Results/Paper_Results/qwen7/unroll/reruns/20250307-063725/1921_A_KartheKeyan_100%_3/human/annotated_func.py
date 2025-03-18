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
        
    #State: Output State: The output state will consist of a series of rounded results from the calculation of the Euclidean distance product between two pairs of points, repeated for each iteration of the while loop until `n` reaches 0.
    #
    #Each iteration of the loop processes four coordinates input by the user, sorts them, calculates the squared Euclidean distances between the first and second points, and the third and fourth points, then computes the square root of these distances multiplied together. The result is printed and rounded to the nearest integer. This process repeats `n` times, decrementing `n` by 1 after each iteration.
    #
    #The final output state will be a list of `n` integers, each representing the rounded result of the distance product calculation for each set of four coordinates provided by the user during the respective iteration of the loop.
#Overall this is what the function does:The function processes a series of square coordinates provided by the user. For each set of coordinates, it calculates the Euclidean distance between the first and second points, and the third and fourth points, multiplies these distances, takes the square root of the product, and prints the rounded result. This process repeats for `n` sets of coordinates, where `n` is the initial value provided by the user. The final output consists of a list of `n` integers, each representing the rounded result of the distance product calculation for each set of coordinates.

