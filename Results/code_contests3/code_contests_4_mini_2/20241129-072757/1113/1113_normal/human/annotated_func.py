#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and each test case consists of 9 lines with 9 characters each, where each character is a digit from '1' to '9' representing a valid sudoku solution.
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
        
    #State of the program after the  for loop has been executed: `t` is equal to `T`, `res` is a list containing `T * 9` strings, each formed from the corresponding input string with all '9's replaced by '1', `row` is the last input string processed, and `nRow` is the modified version of `row` with all '9's replaced by '1'.
    write('\n'.join(res))
#Overall this is what the function does:The function processes a number of test cases, each containing 9 lines of Sudoku solutions. It replaces every occurrence of the digit '9' with '1' in each line and outputs the modified lines. The function does not accept any parameters and writes the results directly to standard output.

