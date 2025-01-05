#State of the program right berfore the function call: **
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `a` is the return value of the last `input()` call, `c` is 0 or 1 depending on the value of `a`, the print statement outputs either -1 or `a / 4 + c`
#Overall this is what the function does:The function does not accept any parameters and iterates over a range of values obtained from user input. For each input value `a`, it checks if `a` is odd, subtracts 9 and sets `c` to 1 if it is. Then, it prints -1 if `a` is in the set (1, 2, 3, 5, 7, 11), otherwise it prints the result of `a / 4 + c`. However, there is a potential missing functionality as the code does not handle the case when the input values are not integers. Additionally, the code does not account for division by zero when `a` is 0.

