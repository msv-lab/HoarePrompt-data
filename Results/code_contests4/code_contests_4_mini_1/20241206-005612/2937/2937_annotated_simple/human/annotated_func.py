#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the subsequent n lines contain either an integer (age in the range 0 to 1000) or a string (drink name with 1 to 100 capital Latin letters).
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `res` is the count of inputs that are either less than 18 or one of the specified alcoholic beverages ('ABSINTH', 'BEER', 'BRANDY', 'CHAMPAGNE', 'GIN', 'RUM', 'SAKE', 'TEQUILA', 'VODKA', 'WISKEY', 'WINE'), and `rep` is `n - 1` after executing all iterations of the loop.
    print(res)
    exit(0)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 100) and processes `n` lines of input. For each input line, if the input is an integer (representing an age between 0 and 1000) and less than 18, or if the input matches any of the specified alcoholic beverages ('ABSINTH', 'BEER', 'BRANDY', 'CHAMPAGNE', 'GIN', 'RUM', 'SAKE', 'TEQUILA', 'VODKA', 'WISKEY', 'WINE'), it increments a counter. After processing all inputs, it prints the count of such inputs. The function does not handle invalid input formats or ages outside the specified range, nor does it validate whether the input is an actual integer or string, which could lead to errors.

