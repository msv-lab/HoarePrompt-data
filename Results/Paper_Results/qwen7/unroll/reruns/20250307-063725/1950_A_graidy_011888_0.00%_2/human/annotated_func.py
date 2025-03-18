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
        
    #State: Output State: The output state will consist of 1000 lines, each containing four elements separated by spaces: three integers (x, y, z) generated randomly between 1 and 9, and a string ('peak', 'stair', or 'none') based on the conditions provided in the loop body.
    #
    #For each line, the first two integers (x and y) are compared. If x is less than y, then y is compared with z:
    #- If y is greater than z, the result is 'peak'.
    #- If y is less than z, the result is 'stair'.
    #- If y is equal to z, the result is 'none'.
    #
    #If x is not less than y (i.e., x is greater than or equal to y), the result is always 'none'.
    #
    #The loop runs 1000 times, so there will be 1000 such lines printed, each describing the outcome of the random comparison for that iteration.
#Overall this is what the function does:The function generates and prints 1000 lines of output. Each line contains three random integers between 1 and 9 and a string ('peak', 'stair', or 'none'). The string is determined based on the comparison of these integers: if the first integer is less than the second and the second is greater than the third, the string is 'peak'; if the first is less than the second and the second is less than the third, the string is 'stair'; otherwise, the string is 'none'. The function does not return any value.

