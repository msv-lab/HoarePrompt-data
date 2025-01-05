#State of the program right berfore the function call: Each test case consists of a 9x9 grid where each cell contains a digit from 1 to 9.**
def func():
    sys.stdout = io.BytesIO()
    atexit.register(lambda : os.write(1, sys.stdout.getvalue()))
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    write = sys.stdout.write
    maxint = float('inf')
    res = []
    T = int(input())
    for t in range(T):
        for i in range(9):
            row = input().strip()
            nRow = ''
            for i in row:
                if i == '9':
                    nRow += '1'
                else:
                    nRow += i
            res.append(nRow)
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, `maxint` is positive infinity, `res` contains modified versions of `row` where every '9' is replaced with '1' and any other character is replaced with its index, `T` remains greater than 0, `t` is equal to `T`, `row` remains unchanged
    write('\n'.join(res))
#Overall this is what the function does:The function `func` does not accept any parameters. It operates on a 9x9 grid where each cell contains a digit from 1 to 9. The function modifies the grid by replacing all '9's with '1's and other digits with their indices. The modified grid is then printed.

