#State of the program right berfore the function call: **Precondition**: 
- n, m, and k are integers such that 1 ≤ n, m, k ≤ 100.
- The instructions for each core are represented by integers xi1, xi2, ..., xim where 0 ≤ xij ≤ k.
def func_1():
    n, m, k = map(int, raw_input().split())
    ins = [([0] * m) for i in xrange(n + 1)]
    cell = [False] * (k + 1)
    nn = [0] * (k + 1)
    core = [0] * (n + 1)
    for i in xrange(n):
        ins[i + 1] = map(int, raw_input().split())
        
    #State of the program after the  for loop has been executed: `n`, `m`, `k`, `ins` is a list of lists with `n + 1` elements each containing `m` integers input by the user, `cell` is a list of `False` values with length `k + 1`, `nn` is a list of `k + 1` zeros, `core` is a list of `n + 1` zeros
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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, the final state will have `core` updated based on the conditions met in the loop, `cell` modified according to the if-else statements, `nn` updated based on the logic in the loop, `d` assigned new values as per the conditions, `i` will be equal to `m`, `m` will maintain its initial positive integer value, `j` will be equal to `n`, `n` will maintain its initial positive integer value, `k` will be at least 1.
    for i in xrange(1, n + 1):
        print(core[i])
        
    #State of the program after the  for loop has been executed: core` is printed at index `n`, `cell` remains unchanged, `nn` remains unchanged, `d` remains unchanged, `i` is equal to `n+1`, `m` maintains its initial positive integer value, `j` is equal to `n+1`, `n` maintains its initial positive integer value, `k` is at least 1.
#Overall this is what the function does:The function `func_1` reads input values for `n`, `m`, and `k`, creates lists `ins`, `cell`, `nn`, and `core` based on the user input. It then iterates through the lists to update the values of `core`, `cell`, `nn`, and `d` according to certain conditions. Finally, it prints the values of `core` at each index from 1 to `n`. The function does not accept any parameters and does not return any value.

