#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each of the t test cases, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000; for each of the t test cases, `a`, `b`, and `c` are integers such that 0 ≤ a, b, c ≤ 9; `i` is 1001; `x`, `y`, and `z` are random integers between 1 and 9 from the last iteration; `res` is determined based on the last values of `x`, `y`, and `z` as per the given conditions.
#Overall this is what the function does:The function generates and prints 1000 sets of three random integers between 1 and 9. For each set, it determines and prints whether the sequence forms a 'peak', 'stair', or 'none' based on specific conditions.

