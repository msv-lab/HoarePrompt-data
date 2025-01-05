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
print(res)
exit(0)