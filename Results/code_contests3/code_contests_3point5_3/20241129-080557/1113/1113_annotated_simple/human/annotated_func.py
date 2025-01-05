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
        
    #State of the program after the  for loop has been executed: `maxint` is positive infinity, `res` is a list containing 9*T identical lists of `nRow`, `T` is the input integer greater than 0, `t` is T-1, `row` is the input string stripped of any leading or trailing whitespaces and not empty, `nRow` consists of '1's in place of '9's in `row` after all iterations of the loop have executed
    write('\n'.join(res))
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `T` representing the number of test cases. For each test case, it reads a 9x9 grid of digits from 1 to 9, replaces '9's with '1's in each row, and stores the modified rows in a list `res`. The function then outputs the modified grid. The functionality is limited to modifying the grid by replacing '9's with '1's.

