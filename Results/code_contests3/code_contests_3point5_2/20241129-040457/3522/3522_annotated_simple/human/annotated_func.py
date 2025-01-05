#State of the program right berfore the function call: Each query input ni is a positive integer greater than 1.**
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `a` is a value greater than 1, `c` is 1 if the last `a` in the loop is odd, otherwise `c` remains 0. The output of the code snippet depends on whether the last `a` in the loop is in the list (1, 2, 3, 5, 7, 11) or not. If it is in the list, then -1 is printed. Otherwise, the result of the last `a / 4 + c` is printed.
#Overall this is what the function does:The function does not accept any parameters. It iterates over a range of values based on user input, performs calculations on each value, and prints the result. If the input value is odd, it subtracts 9 and sets c to 1, then checks if the value is in a predefined list. If the value is in the list, it prints -1; otherwise, it prints the result of the value divided by 4 plus c. The function outputs positive integers greater than 1.

