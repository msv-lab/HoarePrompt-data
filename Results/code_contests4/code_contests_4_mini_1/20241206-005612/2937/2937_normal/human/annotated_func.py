#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, followed by n lines where each line contains either an integer (representing age in the range 0 to 1000) or a string (representing a drink composed of capital Latin letters with a length from 1 to 100). The drinks may include alcohol from the specified list.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `res` is the count of inputs that are either less than 18 or one of the specified alcoholic beverages, `rep` is `n`, and `inp` is the last input string from the user.
    print(res)
    exit(0)
#Overall this is what the function does:The function accepts an integer `n` followed by `n` lines of input, counts how many of those are either underage (less than 18) or names of specified alcoholic drinks, and prints that count. It does not handle unexpected input types or formats.

