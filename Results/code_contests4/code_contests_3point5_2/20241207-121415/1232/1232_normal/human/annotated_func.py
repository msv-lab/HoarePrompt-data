#State of the program right berfore the function call: **
def func():
    stdin = BytesIO(os.read(0, os.fstat(0).st_size))
    stdout = BytesIO()
    res = []
    inp = stdin.readlines()
    T = int(inp[0])
    _i = 1
    for t in range(T):
        N = int(inp[_i])
        
        _i += 1
        
        monsters = []
        
        mnShots = 0
        
        start = maxint
        
        for n in range(N):
            cur = map(int, inp[_i].split())
            _i += 1
            monsters.append(cur)
            if n > 0:
                dam = max(0, cur[0] - monsters[n - 1][1])
                mnShots += dam
                start = min(start, cur[0] - dam)
        
        dam = max(0, monsters[0][0] - monsters[-1][1])
        
        mnShots += dam
        
        start = min(start, monsters[0][0] - dam)
        
        res.append(mnShots + start)
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `stdin` is a BytesIO object containing input from standard input, `stdout` is a new BytesIO object, `res` contains the results of `mnShots + start` for each iteration of the loop, `inp` contains all lines from the input, `T` is greater than 0, `_i` is equal to the total number of lines in `inp`, `N` is assigned the last integer value from the input, `monsters` contains all `cur` values appended in each iteration of the loop, `mnShots` is the sum of the maximum of 0 and the differences between the first elements of each `cur` and the second elements of the previous `cur` in `monsters`, `start` is updated as described above, `n` is equal to `N - 1`, `cur` contains the last set of integers mapped from the last input line, `dam` is calculated as the maximum of 0 and the difference between the first element of `cur` and the second element of the second-to-last element in `monsters`, and the final result of `mnShots + start` for each iteration is stored in `res`.
    os.write(1, '\n'.join(str(x) for x in res))
#Overall this is what the function does:The function `func` reads input from standard input, processes the data according to the provided algorithm, and writes the results to standard output. It calculates and stores specific values based on the input data, but it does not accept any parameters and does not return any value. The function is designed to handle multiple iterations defined by the input data and perform computations accordingly, with the final results being written to standard output.

