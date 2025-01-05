#State of the program right berfore the function call: **
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `a` is assigned the last input value, `c` is 1 if the last `a` input is an odd integer, and the code prints -1 if the last `a` input is in (1, 2, 3, 5, 7, 11). Otherwise, it prints the result of the last `a / 4 + c`
#Overall this is what the function does:The function `func` reads multiple inputs and performs specific calculations based on the input values. It first checks if the input value is odd, subtracts 9 if it is, updates a flag `c` accordingly. Then, it prints -1 if the input is in a predefined set, otherwise, it prints the result of dividing the input by 4 and adding `c`. The function does not have explicit return values, it performs the calculations and prints the outputs directly.

