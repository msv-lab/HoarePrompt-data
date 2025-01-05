#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and for each of the following n lines, each line contains either an integer (age) from 0 to 1000 or a string (drink) of capital Latin letters with a length from 1 to 100.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `res` is the count of inputs that are either less than 18 or one of the specified alcoholic beverages, `rep` is `n`.
    print(res)
    exit(0)
#Overall this is what the function does:The function accepts an integer input `n` (between 1 and 100) and then processes `n` lines of input, where each line can either be an integer (representing age, from 0 to 1000) or a string (representing a drink name). It counts how many of these inputs are either ages less than 18 or one of the specified alcoholic beverages (such as 'ABSINTH', 'BEER', 'BRANDY', etc.). After processing all inputs, it prints the total count of such inputs.

