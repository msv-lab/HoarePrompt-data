#State of the program right berfore the function call: n is a positive integer. Each ti is a positive integer and diri is a string that is one of: "North", "South", "West", "East".**
def func():
    HEIGHT = 20000
    f = sys.stdin
    height = HEIGHT
    n = int(f.readline())
    sat = True
    for i in range(n):
        dst, directon = f.readline().strip().split(' ')
        
        if directon not in {'South', 'North'}:
            continue
        
        if directon == 'South':
            height -= int(dst)
        elif directon == 'North':
            height += int(dst)
        else:
            raise ValueError('Invalid directon')
        
        if height < 0 or height > HEIGHT:
            sat = False
            break
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, each `ti` is a positive integer, `diri` is a string that is one of: "North", "South", "West", "East", `HEIGHT` is 20000, `f` is assigned to sys.stdin, `height` is within the range of 0 to 20000, `sat` is True if the height remains within the valid range after all iterations of the loop. If at any point the height goes below 0 or exceeds HEIGHT, `sat` is False
    sat &= height == HEIGHT
    print('YES' if sat else 'NO')
#Overall this is what the function does:The function does not accept any parameters. It reads input from the standard input, calculates the final height of a point based on a sequence of movements, and checks if the final height is equal to the predefined HEIGHT value. It then prints 'YES' if the final height is equal to HEIGHT, and 'NO' otherwise. The function ensures that the direction of movement is either 'North' or 'South'. If the height goes below 0 or exceeds HEIGHT during the movements, it sets the satisfaction flag to False. If the height is within the valid range after all movements, it sets the satisfaction flag to True. If the final height matches HEIGHT and the satisfaction flag is True, it prints 'YES', otherwise it prints 'NO'.

