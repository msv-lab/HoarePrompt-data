#State of the program right berfore the function call: **
def func_1():
    n, m, k = map(int, raw_input().split())
    ins = [([0] * m) for i in xrange(n + 1)]
    cell = [False] * (k + 1)
    nn = [0] * (k + 1)
    core = [0] * (n + 1)
    for i in xrange(n):
        ins[i + 1] = map(int, raw_input().split())
        
    #State of the program after the  for loop has been executed: `n`, `m`, `k`, `ins`, `cell`, `nn`, and `core` are determined by the input values, and `ins` contains the mapped integers from the input split by spaces for each index from 1 to n
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
        
    #State of the program after the  for loop has been executed: Output State: After all iterations of the loop have finished, the variables `n`, `m`, `k`, `ins`, `cell`, `nn`, `core`, `i`, `j`, and `d` will have been updated based on the conditions specified in the loop. The final state will depend on the input values and the logic within the loop. The values of `nn[j]`, `core[j]`, `d`, `cell[d]`, `j`, `n`, and `k` will be determined by the conditions evaluated in each iteration of the loop.
    for i in xrange(1, n + 1):
        print(core[i])
        
    #State of the program after the  for loop has been executed: All `core` values from `core[1]` to `core[n]` will be printed in sequence. The values of `i` will go from 1 to `n`, where `n` is the input value. The values of `nn[j]`, `d`, `cell[d]`, `j`, and `k` are not affected by the loop.
#Overall this is what the function does:The function `func_1` reads input values for `n`, `m`, and `k`, then populates the lists `ins`, `cell`, `nn`, and `core` accordingly. It processes these lists through nested loops, updating the values based on certain conditions. Finally, it prints the values of `core` from `core[1]` to `core[n]` sequentially. The function does not accept any parameters and does not return any value.

