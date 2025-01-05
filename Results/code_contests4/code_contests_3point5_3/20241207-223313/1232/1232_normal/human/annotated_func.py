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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `stdin` contains the input read from standard input, `stdout` is a BytesIO object, `res` contains the appended values of `mnShots + start` for each iteration, `inp` is a list containing the lines read from standard input, `T` is greater than 0, `_i` is equal to the total number of elements in `inp`, `t` is the total number of elements in `inp`, `N` is assigned the last integer value in the list `inp`, `monsters` contains all the maps of integers extracted from the split elements of `inp`, `mnShots` is the total sum of all `dam` values calculated throughout the loop, `start` is the minimum value between all the `cur[0] - dam` results, `n` is equal to `N - 1`, `cur` is a map object with integer values extracted from the split elements of the last element of `inp`, `dam` is the result of the calculation `max(0, monsters[0][0] - monsters[-1][1])`.
    os.write(1, '\n'.join(str(x) for x in res))
#Overall this is what the function does:The function reads input from standard input, processes the data to calculate certain values related to monsters, and then writes the results to standard output. It iterates through a loop for a specified number of test cases, calculates values based on the input data, and appends the results to a list. Finally, it writes the calculated results to standard output. The function does not accept any parameters and does not return any value.

