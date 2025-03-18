#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, a, b, and c are integers such that 0 <= a, b, c <= 9.
def func():
    i = 1
    while i <= 1000:
        x = randint(1, 9)
        
        y = randint(1, 9)
        
        z = randint(1, 9)
        
        res = ''
        
        if x < y:
            if y > z:
                res = 'peak'
            elif y < z:
                res = 'stair'
            else:
                res = 'none'
        else:
            res = 'none'
        
        print(x, y, z, sep=' ')
        
        print(res)
        
        i += 1
        
    #State: The loop will have printed 1000 lines, each consisting of three random integers between 1 and 9, followed by one of the strings 'peak', 'stair', or 'none'. The variables `x`, `y`, `z`, and `res` will hold the values from the last iteration of the loop. The variable `i` will be 1001. The variables `t`, `a`, `b`, and `c` will remain unchanged.
#Overall this is what the function does:The function prints 1000 lines, each consisting of three random integers between 1 and 9, followed by one of the strings 'peak', 'stair', or 'none'. The strings 'peak' and 'stair' are determined based on the relative values of the three integers, while 'none' indicates no specific increasing or decreasing order. The function does not accept any parameters and does not return any value.

