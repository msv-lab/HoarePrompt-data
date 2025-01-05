#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100. Each visitor's age is an integer from 0 to 1000, and each visitor's drink is a string of capital Latin letters from 1 to 100 in length. Only the drinks from the list given in the problem description should be considered alcohol.**
def func():
    n = int(raw_input())
    res = 0
    for rep in range(n):
        inp = raw_input()
        
        if inp[0] >= '0' and inp[0] <= '9':
            if int(inp) < 18:
                res = res + 1
        elif inp == 'ABSINTH':
            res = res + 1
        elif inp == 'BEER':
            res = res + 1
        elif inp == 'BRANDY':
            res = res + 1
        elif inp == 'CHAMPAGNE':
            res = res + 1
        elif inp == 'GIN':
            res = res + 1
        elif inp == 'RUM':
            res = res + 1
        elif inp == 'SAKE':
            res = res + 1
        elif inp == 'TEQUILA':
            res = res + 1
        elif inp == 'VODKA':
            res = res + 1
        elif inp == 'WISKEY':
            res = res + 1
        elif inp == 'WINE':
            res = res + 1
        
    #State of the program after the  for loop has been executed: `res` is the count of inputs that meet specific conditions, `rep` is the number of iterations of the loop, `n` is greater than 0, and `inp` is assigned a specific value after each iteration. The final value of `res` depends on the input values that meet the specified conditions throughout all iterations of the loop.
    print(res)
    exit(0)
#Overall this is what the function does:The function `func` reads an integer `n` from input and then processes a list of `n` visitor entries. Each visitor entry consists of an age (an integer from 0 to 1000) and a drink (a string of capital Latin letters from 1 to 100 in length). The function checks if the drink is classified as alcohol and if the age is under 18. It increments a counter `res` for each visitor entry that meets these conditions. Finally, the function prints the total count of visitors who meet the specified conditions. However, there is a potential missing functionality in the code. The code does not handle cases where the input drink is not of the specified alcohol types, potentially leading to inaccurate results. This missing logic could affect the overall functionality of the function.

