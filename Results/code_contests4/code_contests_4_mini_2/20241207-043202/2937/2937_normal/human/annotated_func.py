#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100, and each of the following n lines contains either an integer representing age (0 <= age <= 1000) or a string representing a drink (1 <= length of drink <= 100) consisting of capital Latin letters. The drinks must be checked against the defined list of alcoholic beverages.
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
        
    #State of the program after the  for loop has been executed: `res` is the count of inputs that are either less than 18 or are one of the specified alcoholic beverages ('ABSINTH', 'BEER', 'BRANDY', 'CHAMPAGNE', 'GIN', 'RUM', 'SAKE', 'TEQUILA', 'VODKA', 'WISKEY', 'WINE'); `n` is within the range of 1 to 100; `rep` is equal to `n - 1` after all iterations, indicating the number of times the loop has executed.
    print(res)
    exit(0)
#Overall this is what the function does:The function accepts an integer `n` indicating the number of subsequent inputs, which can either be an age or a drink name. It counts how many of the inputs are either ages less than 18 or names of specified alcoholic beverages (ABSINTH, BEER, BRANDY, CHAMPAGNE, GIN, RUM, SAKE, TEQUILA, VODKA, WISKEY, WINE). The final count is printed as output.

