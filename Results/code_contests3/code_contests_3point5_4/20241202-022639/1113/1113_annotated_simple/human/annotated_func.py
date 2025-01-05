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
        
    #State of the program after the  for loop has been executed: `maxint` is positive infinity, `res` contains the modified `nRow` after all iterations of the loop, `i` is the last element in `row`, `row` contains the modified stripped input value after all iterations, `nRow` contains the result of replacing all occurrences of '9' with '1' in the original input `row` for all elements in `T`, `t` is equal to `T`
    write('\n'.join(res))
#Overall this is what the function does:The function `func` reads input from standard input, modifies the input by replacing all occurrences of '9' with '1', and outputs the modified grid. The function does not accept any parameters and does not return any value.

