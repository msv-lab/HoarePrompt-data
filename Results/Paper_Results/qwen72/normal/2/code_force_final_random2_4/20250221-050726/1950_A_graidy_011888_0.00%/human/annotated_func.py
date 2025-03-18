#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are integers such that 0 <= a, b, c <= 9.
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
        
    #State: After the loop executes all 1000 iterations, `t` is an integer such that 1 <= t <= 1000, `a`, `b`, and `c` are integers such that 0 <= a, b, c <= 9, `i` is 1001, `x`, `y`, and `z` are random integers between 1 and 9 (inclusive) for each iteration. For each iteration, if `x` < `y` and `y` > `z`, `res` is 'peak'. If `x` < `y` and `y` < `z`, `res` is 'stair'. If `x` < `y` and `y` == `z`, `res` is 'none'. If `x` >= `y`, `res` is 'none'.
#Overall this is what the function does:The function `func` generates 1000 sets of three random integers (`x`, `y`, `z`) between 1 and 9 (inclusive). For each set, it determines a string result (`res`) based on the relationships between these integers: if `x` is less than `y` and `y` is greater than `z`, `res` is 'peak'; if `x` is less than `y` and `y` is less than `z`, `res` is 'stair'; otherwise, `res` is 'none'. The function prints each set of integers followed by the corresponding `res`. After 1000 iterations, the function completes without returning any value.

