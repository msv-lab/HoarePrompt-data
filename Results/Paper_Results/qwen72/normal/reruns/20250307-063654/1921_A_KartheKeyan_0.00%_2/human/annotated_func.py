#State of the program right berfore the function call: The function `func` should take a list of test cases as input, where each test case is a list of 4 tuples, each tuple containing two integers (x_i, y_i) representing the coordinates of the corners of a square. The integers x_i and y_i are within the range -1000 to 1000, inclusive. The number of test cases, t, is an integer such that 1 <= t <= 100. Each test case is guaranteed to form a square with sides parallel to the coordinate axes and with a positive area.
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
        
    #State: `n` is 0, `s` is the last calculated value based on the input `l`, `coord` is a list containing 4 tuples, each tuple representing a pair of input integers, but now sorted in ascending order based on the first element of each tuple, `res` is the absolute value of the product of the square roots of `p1` and `p2`, `i` is 3, `x` and `y` are updated to the last input integers, `p1` is the squared Euclidean distance between the first and second tuples in the sorted list, `p2` is the squared Euclidean distance between the third and fourth tuples in the sorted list.
#Overall this is what the function does:The function `func` reads an integer `n` indicating the number of test cases. For each test case, it reads 4 pairs of integers representing the coordinates of the corners of a square. It then calculates and prints the area of the square formed by these coordinates. The function does not return any value but prints the area for each test case. After processing all test cases, the function terminates with `n` set to 0.

