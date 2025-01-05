#State of the program right berfore the function call: Each test case consists of a 9×9 grid where each cell contains a digit from 1 to 9.**
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
        
    #State of the program after the  for loop has been executed: Output State: `maxint` is positive infinity, `res` contains the final appended values of all `nRow` from each iteration, `row` is the input value from the last iteration, `nRow` contains the final value obtained after replacing all occurrences of '9' with '1' in `row`, `t` is the last iteration number, `T` is equal to the final `t` value, `i` is the last character iterated over in `row`.
    write('\n'.join(res))
#Overall this is what the function does:The function `func` does not accept any parameters. It processes a 9x9 grid where each cell contains a digit from 1 to 9. The function replaces all occurrences of '9' with '1' in each row of the grid and prints the modified grid. The function does not explicitly return any value.

