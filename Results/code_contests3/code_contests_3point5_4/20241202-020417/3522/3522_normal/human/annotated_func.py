#State of the program right berfore the function call: **
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `a` is updated based on the inputs provided, `c` is set to 1 if the last input is odd, the print statement outputs -1 if the last input is in (1, 2, 3, 5, 7, 11), otherwise it outputs the last input divided by 4 plus `c`
#Overall this is what the function does:The function does not accept any parameters explicitly. It iterates over the user-provided inputs, updates the value of `a` based on the input, sets `c` to 1 if the updated `a` is odd, then prints either -1 if the updated `a` is in (1, 2, 3, 5, 7, 11), or the updated `a` divided by 4 plus `c`.

