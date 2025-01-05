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
        
    #State of the program after the  for loop has been executed: `n`, `ti`, `diri`, `dir`, `diri`, `dst`, `i`, `f`, `sat` are all positive integers/strings/constants. If `height` is less than 0 or greater than `HEIGHT`, `sat` is False. If `direction` = 'South', `height` is decreased by the integer value obtained from `dst`. If `direction` = 'North', `height` is increased by the integer value of `dst`. If `direction` is not in {'South', 'North'}, no changes occur in the program state.
    sat &= height == HEIGHT
    print('YES' if sat else 'NO')
#Overall this is what the function does:The function does not accept any parameters. It reads input from the standard input, processes a series of movements (North or South) with corresponding distances, updates the height based on the movements, and checks if the final height is equal to the predefined constant HEIGHT. If the final height matches HEIGHT, it prints 'YES'; otherwise, it prints 'NO'.

