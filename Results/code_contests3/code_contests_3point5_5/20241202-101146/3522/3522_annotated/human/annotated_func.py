#State of the program right berfore the function call: **
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: The final value of `c` will be 1 if at least one of the input values was odd; otherwise, it will remain 0.
#Overall this is what the function does:The function does not accept any parameters. It iterates over a specified number of input values. For each input value, it checks if the value is odd, subtracts 9 from it if it is odd, sets a flag `c` to 1 if the value was odd, and then prints -1 if the value is in the set (1, 2, 3, 5, 7, 11), otherwise it prints the value divided by 4 plus the flag `c`. The final value of `c` will be 1 if at least one of the input values was odd; otherwise, it will remain 0.

