#State of the program right berfore the function call: n is a positive integer representing the number of bar's clients. Each client's age is an integer between 0 and 1000, or their drink is a string of capital Latin letters from 1 to 100 in length.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `rep` ranges from 0 to `n-1`, `inp` is assigned the input value. If `inp[0]` is a digit between '0' and '9' and `int(inp)` < 18, `res` is incremented by 1. If `inp` is 'ABSINTH', 'BEER', 'BRANDY', 'CHAMPAGNE', 'GIN', 'RUM', 'SAKE', 'TEQUILA', 'VODKA', 'WISKEY', or 'WINE', `res` is incremented by 1. Otherwise, `res` remains unchanged
    print(res)
    exit(0)
#Overall this is what the function does:The function reads the number of clients `n` as input and then iterates `n` times to process information about each client. If the client's input starts with a digit between '0' and '9' and the input is less than 18, or the input matches specific drink names, the counter `res` is incremented. Finally, the function prints the total count `res` and exits. The function does not accept any parameters and does not return any specific value.

