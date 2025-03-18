#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: i is 1001, and the values of t, a, b, and c remain unchanged.
#Overall this is what the function does:The function generates and prints 1000 sets of three random integers between 1 and 9. For each set, it determines if the middle integer is a peak (greater than the other two) or part of a stair (greater than one and less than the other), and prints the result. The input parameters `t`, `a`, `b`, and `c` are not used in the function.

