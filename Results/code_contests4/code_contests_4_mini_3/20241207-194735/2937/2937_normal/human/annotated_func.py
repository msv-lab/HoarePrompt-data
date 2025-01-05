#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100, and the subsequent n lines contain either an integer representing age (0 to 1000) or a string representing a drink (1 to 100 characters long) which consists of capital Latin letters. The drinks considered alcoholic are: ABSINTH, BEER, BRANDY, CHAMPAGNE, GIN, RUM, SAKE, TEQUILA, VODKA, WHISKEY, WINE.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 100; `res` is the count of inputs that are either a number less than 18 or one of the specified alcoholic beverages; `rep` is equal to `n`.
    print(res)
    exit(0)
#Overall this is what the function does:The function accepts an integer `n` representing the number of subsequent lines of input, which may contain either ages (0 to 1000) or names of drinks (alcoholic beverages). It counts how many of the inputs represent minors (ages less than 18) or are alcoholic drinks from a specified list, and prints this count. The function does not handle invalid inputs or non-integer values and assumes the input will be correctly formatted.

