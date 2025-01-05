#State of the program right berfore the function call: **Precondition**: **n, m, k are integers such that 1 ≤ n, m, k ≤ 100. The instructions for each core are represented as integers xi1, xi2, ..., xim where 0 ≤ xij ≤ k.**
def func_1():
    n, m, k = map(int, raw_input().split())
    ins = [([0] * m) for i in xrange(n + 1)]
    cell = [False] * (k + 1)
    nn = [0] * (k + 1)
    core = [0] * (n + 1)
    for i in xrange(n):
        ins[i + 1] = map(int, raw_input().split())
        
    #State of the program after the  for loop has been executed: `n`, `m`, and `k` are integers such that 1 ≤ n, m, k ≤ 100; `ins` is a 2D list of dimensions (n+1) x m with values taken from user input for all rows; `cell` is a list of `False` values with a length ranging from 2 to 101; `nn` is a list of `0` values with a length ranging from 1 to 101; `core` is a list of 0 values with a length of (n + 1)
    for i in xrange(m):
        for j in xrange(1, k + 1):
            nn[j] = 0
        
        for j in xrange(1, n + 1):
            if core[j] == 0:
                d = ins[j][i]
                if d != 0:
                    if cell[d]:
                        core[j] = i + 1
                    elif nn[d] != 0:
                        cell[d] = True
                        core[j] = core[nn[d]] = i + 1
                        nn[d] = j
                    elif nn[d] == 0:
                        nn[d] = j
        
    #State of the program after the  for loop has been executed: At the end of the loop execution, the values of `k`, `nn`, `n`, `j`, `d`, `ins[j][i]`, `core[j]`, `cell[d]`, and `nn[d]` will be appropriately updated based on the conditions within the loop. The final state will depend on the specific conditions met during all iterations of the loop.
    for i in xrange(1, n + 1):
        print(core[i])
        
    #State of the program after the  for loop has been executed: At the end of the loop execution, the values of `k`, `nn`, `n`, `j`, `d`, `ins[j][i]`, `core[j]`, `cell[d]`, and `nn[d]` are appropriately initialized or updated based on the loop conditions. The loop will print the values of `core` from `core[1]` to `core[n]` sequentially.
#Overall this is what the function does:The function `func_1` reads user input for `n`, `m`, and `k`, initializes various lists based on the input values, processes the input data through nested loops to update core values, and then prints the core values from `core[1]` to `core[n]`. The function does not accept any parameters, and its output is the printed core values.

