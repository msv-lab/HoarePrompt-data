#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, there are 9 lines of strings containing exactly 9 characters each, where each character is a digit from '1' to '9'.
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
        
    #State of the program after the  for loop has been executed: `res` contains `9 * T` strings with all '9's replaced by '1's, `nRow` is the last modified string from the final `row`, `row` is the last input string after stripping whitespace, `i` is the last character of `row`, and `t` is `T`.
    write('\n'.join(res))
#Overall this is what the function does:The function accepts an integer `T`, which indicates the number of test cases, and processes `T` grids, each consisting of 9 strings of digits from '1' to '9'. For each string, it replaces every occurrence of '9' with '1', and then outputs the modified strings. The function effectively transforms the input grid by altering the character '9' and returns the result as a single output containing all modified rows for each test case.

