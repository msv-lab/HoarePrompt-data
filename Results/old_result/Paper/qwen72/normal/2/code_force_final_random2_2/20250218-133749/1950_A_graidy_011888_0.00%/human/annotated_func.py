#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, and for each test case, a, b, and c are integers where 0 <= a, b, c <= 9.
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
        
    #State: t is an integer where 1 <= t <= 1000, a, b, and c are integers where 0 <= a, b, c <= 9, i is 1001. For each iteration from 1 to 1000, x, y, and z were random integers between 1 and 9 (inclusive). The value of res was determined based on the conditions: if x < y, then if y > z, res was 'peak'; if y < z, res was 'stair'; if y == z, res was 'none'. If x >= y, res was 'none'.
#Overall this is what the function does:The function `func` generates and prints 1000 sets of three random integers (x, y, z) between 1 and 9 (inclusive). For each set, it determines and prints a string (`res`) based on the following conditions: if `x < y` and `y > z`, `res` is 'peak'; if `x < y` and `y < z`, `res` is 'stair'; otherwise, `res` is 'none'. After 1000 iterations, the function completes without returning any value. The state of the program after the function concludes includes `i` being 1001, and the values of `t`, `a`, `b`, and `c` remain unchanged.

