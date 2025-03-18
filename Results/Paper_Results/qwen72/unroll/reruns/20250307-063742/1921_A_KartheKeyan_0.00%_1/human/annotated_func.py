#State of the program right berfore the function call: The function should take a list of tuples as input, where each tuple represents the coordinates of a corner of the square. The list contains exactly four tuples, and each tuple consists of two integers (x_i, y_i) such that -1000 <= x_i, y_i <= 1000. The coordinates represent a square with sides parallel to the coordinate axes and with a positive area.
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
        
    #State: `n` is 0, `l` is the last input integer, `s` is the last calculated value of `(l//4) + (l - (4 * (l//4))) // 2`, and the list of tuples representing the coordinates of the square remains unchanged.
#Overall this is what the function does:The function repeatedly reads an integer `n` from the user and for each value of `n`, it reads four pairs of integers representing the coordinates of the corners of a square. It then calculates and prints the area of the square. After processing `n` squares, the function terminates with `n` set to 0. The function does not return any value.

