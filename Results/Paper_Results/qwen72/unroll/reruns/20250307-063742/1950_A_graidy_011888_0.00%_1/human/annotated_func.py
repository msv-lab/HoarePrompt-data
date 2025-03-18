#State of the program right berfore the function call: The function is expected to handle multiple test cases, where each test case consists of three digits a, b, and c such that 0 <= a, b, c <= 9. The number of test cases, t, is a positive integer where 1 <= t <= 1000.
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
        
    #State: The loop will have executed 1000 times, generating and printing three random integers (x, y, z) between 1 and 9 for each iteration, followed by the string 'peak', 'stair', or 'none' based on the conditions specified. The variable `i` will be 1001, and the values of `t`, `a`, `b`, and `c` will remain unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It generates 1000 test cases, each consisting of three random integers (x, y, z) between 1 and 9. For each test case, it prints the three integers followed by a string indicating the relationship between them: 'peak' if y is greater than both x and z, 'stair' if y is less than both x and z, and 'none' otherwise. After 1000 iterations, the function concludes without modifying any external variables.

