#State of the program right berfore the function call: Each test case consists of 9 lines, each line consists of 9 characters from 1 to 9 without any whitespaces.**
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
        
    #State of the program after the  for loop has been executed: `maxint` is the float representation of positive infinity, `T` is greater than 0, `t` is equal to `T-1`, `row` contains the stripped input value, `nRow` contains the value of `row` after replacing all occurrences of '9' with '1', `res` contains a list of concatenated strings of `nRow` after each iteration of the loop, `i` is the last element in `row` appended with '1' if i == '9', otherwise appended with the values of `i`
    write('\n'.join(res))
#Overall this is what the function does:The function `func` reads input data, replaces all occurrences of '9' with '1' in each line, and concatenates the modified lines to form a result. The function does not accept any parameters. The result is then written to the standard output.

