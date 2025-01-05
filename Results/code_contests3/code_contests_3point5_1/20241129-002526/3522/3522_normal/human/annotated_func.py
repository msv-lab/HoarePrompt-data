#State of the program right berfore the function call: Each query integer ni is a positive integer greater than 1.**
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: Output State: Each query integer `n` is a positive integer greater than 1, `_` is equal to the total number of iterations of the loop, `a` is the last input value entered, `c` is 1 if the last `a` is odd. The code prints -1 if the last `a` is in the set (1, 2, 3, 5, 7, 11), otherwise it prints the result of the last `a` divided by 4 plus the sum of all `c` values encountered during the loop execution.
#Overall this is what the function does:The function does not accept any parameters. It iterates over a sequence of queries, where each query integer `a` is a positive integer greater than 1. If `a` is odd, it subtracts 9 and increments the count `c` by 1. It then prints -1 if `a` is in the set {1, 2, 3, 5, 7, 11}, otherwise it prints the result of `a` divided by 4 plus the sum of all `c` values encountered during the loop execution.

