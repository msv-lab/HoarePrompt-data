#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100.**
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= 100, `res` is an integer. After all iterations of the loop have finished, `res` will be the total number of occurrences where the conditions are met in the loop for all inputs provided.
    print(res)
    exit(0)
#Overall this is what the function does:The function `func` reads an integer `n` as input, then reads `n` strings and counts the occurrences of specific strings meeting certain conditions. It then prints the total count of occurrences. The function does not return any value.

