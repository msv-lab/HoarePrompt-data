#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: Output State: The output state will consist of 1000 lines, each containing four elements: three integers between 1 and 9 (inclusive) representing `x`, `y`, and `z`, and a string representing `res`. 
    #
    #The first two integers (`x` and `y`) will be compared, and based on their relationship, the third integer (`z`), and the value of `res` will be determined as follows:
    #- If `x < y` and `y > z`, then `res` will be 'peak'.
    #- If `x < y` and `y < z`, then `res` will be 'stair'.
    #- If `x < y` and `y == z`, or if `x >= y`, then `res` will be 'none'.
    #
    #Each line will be formatted as `x y z res`, where `x`, `y`, and `z` are randomly generated integers from 1 to 9, and `res` is one of the strings 'peak', 'stair', or 'none'.
#Overall this is what the function does:The function generates and prints 1000 lines of output. Each line contains three random integers between 1 and 9 (inclusive) and a string ('peak', 'stair', or 'none'). The string is determined based on the comparison of these integers: if the first integer is less than the second and the second is greater than the third, the string is 'peak'; if the first is less than the second and the second is less than the third, the string is 'stair'; otherwise, the string is 'none'. The function does not return any value.

