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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `res` will be a list of strings where each string is obtained by replacing all occurrences of '9' with '1' based on the characters in the corresponding input string `row`. All other variables remain the same as the initial state.
    write('\n'.join(res))
#Overall this is what the function does:The function `func` reads input consisting of 9 lines, each containing 9 characters from '1' to '9'. It then replaces all occurrences of '9' with '1' in each input string and stores the modified strings in a list `res`. Finally, it prints the modified strings separated by newlines. The function does not accept any parameters and does not have specified return values.

